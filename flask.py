# Importando la clase Flask
from flask import Flask

# Creando función de control
def create_app():

    # Creando la variable de iniciación
    app = Flask(__name__)

    # Configuración del proyecto
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev_esit'
    )

    # Definiendo rutas
    @app.route('/')
    def index():
        return 'Hola Mundo'

    return app
