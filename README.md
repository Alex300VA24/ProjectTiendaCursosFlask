
# 🛒 Tienda de Cursos de Computación Online con Flask


Este proyecto es una plataforma web para una **tienda de cursos online**, desarrollada en **Python** usando el microframework **Flask**, para la base de datos **Mysql**. Para la interfaz se utilizan tecnologías modernas como **HTML5**, **CSS**, **JavaScript** y el framework de diseño **Bootstrap** para una experiencia de usuario clara y profesional.


---

## ⚙️ Pasos para ejecutar el proyecto localmente

Sigue estas instrucciones paso a paso para clonar, configurar y ejecutar el proyecto en tu entorno de desarrollo:

---

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/usuario/tienda-cursos-flask.git
cd projectTiendaCursosFlask
```

---

### 2️⃣ Crear un entorno virtual

```bash
python -m venv venv
```

---

### 3️⃣ Activar el entorno virtual

#### En Windows (PowerShell):

```bash
.env\Scripts\Activate
```

#### En Linux/Mac:

```bash
source venv/bin/activate
```

---

### 4️⃣ Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Crear el archivo `.env`

En la raíz del proyecto, crea un archivo llamado `.env` y agrega:

```env
MAIL_PASSWORD='contrasenaEjemplo'
```

Este valor es usado para autenticar el envío de correos.

---

### 6️⃣ Crear la base de datos MySQL

Debes tener instalado **MySQL** y ejecutar el archivo `tienda.sql` para crear la base de datos y sus tablas.

#### Opción 1: Usando la terminal de MySQL

```bash
mysql -u tu_usuario -p < tienda.sql
```

#### Opción 2: Usando MySQL Workbench

1. Abre MySQL Workbench.
2. Conéctate a tu servidor.
3. Abre el archivo `tienda.sql`.
4. Ejecuta el script.

#### Opción 3: Usando phpMyAdmin

1. Abre phpMyAdmin en tu navegador.
2. Selecciona "Importar".
3. Elige el archivo `tienda.sql`.
4. Haz clic en "Continuar".

---

### 7️⃣ Definir el módulo principal de ejecución

En PowerShell, define el archivo principal desde donde se ejecutará la app:

```bash
$env:FLASK_APP = "cli.py"
```

---

### 8️⃣ (Opcional) Activar el modo debug

Para ver errores detallados durante el desarrollo:

```bash
$env:FLASK_DEBUG = 1
```

---

### 9️⃣ Configurar destinatarios del correo

En el archivo `mails.py`, puedes especificar a qué correo se enviarán los mensajes:

```python
recipients = ['correo_destino@ejemplo.com']
```

---

### 🔟 Configurar el correo de envío

En `cli.py` o en el archivo `configuracion.py`, establece el correo desde el cual se enviarán los mensajes:

```python
MAIL_USERNAME = 'correo_origen@ejemplo.com'
```

---

## ✅ ¡Todo listo!

Ejecuta tu aplicación con:

```bash
flask run
```

Abre tu navegador y visita `http://localhost:5000` para ver tu **Tienda de Cursos de Computación Online** funcionando.

---
