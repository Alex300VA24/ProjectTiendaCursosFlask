from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mail import Mail
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector

def get_db_connection():
        return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tienda"
    )

from .models.ModeloCompra import ModeloCompra
from .models.ModeloUsuario import ModeloUsuario
from .models.ModeloCurso import ModeloCurso

from .models.entities.Compra import Compra
from .models.entities.Curso import Curso
from .models.entities.Usuario import Usuario
#from werkzeug.security import generate_password_hash, check_password_hash

from .conts import * 
from .emails import confirmacion_compra


app = Flask(__name__)

csrf = CSRFProtect()

db = MySQL(app)
login_manager_app = LoginManager(app)
mail = Mail()



@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.obtener_por_id(db, id)



@app.route('/login', methods=['GET', 'POST'])
def login():
    
    # CSRF Cross Site Request Forgery == Solicitud de falsificacion entre sitios
    if request.method == 'POST':
        print(request.form['usuario'])
        print(request.form['password'])
        usuario = Usuario(
            None, request.form['usuario'], request.form['password'], None)
        usuario_logeado = ModeloUsuario.login(db, usuario)
        print(usuario_logeado)
        if usuario_logeado != None:
            login_user(usuario_logeado)
            flash(BIENVENIDA, 'success')
            return redirect(url_for('panel'))
        else:
            
            flash(LOGIN_CREDENCIALES_INVALIDAS,'warning')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')
    
@app.route('/logout')
def logout():
    logout_user()
    flash(LOGOUT, 'success')
    return redirect(url_for('login'))

@app.route('/sing_up', methods=['GET', 'POST'])
def sing_up():
    if request.method == 'POST':
        usuario = Usuario(None, request.form['usuario'], request.form['password'], None)

        resultado = ModeloUsuario.registrar(db, usuario)

        if resultado == 'existe':
            flash('El usuario ya existe, elige otro nombre.', 'warning')
            return render_template('auth/sing_up.html')

        elif resultado == 'ok':
            flash('Usuario registrado exitosamente. Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))

        else:
            flash('Ocurrió un error en el registro.', 'danger')
            return render_template('auth/sing_up.html')

    return render_template('auth/sing_up.html')

'''@app.route('/password/<password>')
def generar_password(password):
    encriptado = generate_password_hash(password)
    #valor = check_password_hash(encriptado, password)
    return f"Encriptado: {encriptado} | Longitud: {len(encriptado)}"'''

@app.route('/')
#@login_required
def index():
    return render_template('plantilla.html')

@app.route('/panel')
@login_required
def panel():
    if current_user.is_authenticated:
        if current_user.tipousuario.id == 1:
            try:
                cursos_vendidos = ModeloCurso.listar_cursos_vendidos(db)
                data = {
                    'titulo':'Cursos Vendidos:',
                    'cursos_vendidos': cursos_vendidos
                }
                return render_template('index.html', data=data)
            except Exception as ex:
                return render_template('errores/error.html', mensaje=format(ex))
        else:
            try:    
                compras = ModeloCompra.listar_compras_usuario(db, current_user)
                data = {
                    'titulo': 'Mis compras:',
                    'compras': compras
                }
                return render_template('index.html', data=data)
            except Exception as ex:
                return render_template('errores/error.html', mensaje=format(ex))
    else:
        return redirect(url_for('login'))

@app.route('/cursos')
@login_required
def listar_cursos():
    try:
        cursos = ModeloCurso.listar_cursos(db)
        
        data = {
            'titulo': 'Listado de Cursos',
            'cursos': cursos
        }
        return render_template('listado_cursos.html', data=data)
    except Exception as ex:
        return render_template('errores/error.html', mensaje=format(ex))

@app.route('/comprarCurso', methods=['POST'])
@login_required
def comprar_curso():
    data_request = request.get_json()
    data = {}
    try:
        #curso = Curso(data_request['id'], None, None, None, None)
        curso = ModeloCurso.leer_curso(db, data_request['id'])
        compra = Compra(None, curso, current_user)
        data['exito'] = ModeloCompra.registrar_compra(db, compra)
        # confirmacion_compra(mail, current_usser, curso)
        confirmacion_compra(app, mail, current_user, curso)
    except Exception as ex:
        data['mensaje'] = format(ex)
        data['exito'] = False
    return jsonify(data)

def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404
def pagina_no_autorizada(error):
    return redirect(url_for('login'))

def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    mail.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    app.register_error_handler(401, pagina_no_autorizada)
    return app
