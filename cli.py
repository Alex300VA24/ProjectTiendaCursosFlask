import os
from flask.cli import FlaskGroup
from app import inicializar_app
from configuracion import configuracion

# Configurar variable de entorno FLASK_DEBUG
os.environ["FLASK_DEBUG"] = "1"


config_cli = configuracion['development']

app = inicializar_app(config_cli)

cli = FlaskGroup(app)



if __name__ =='__main__':
    cli()