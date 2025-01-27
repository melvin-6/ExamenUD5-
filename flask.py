# Importando la clase Flask
from flask import Flask

# Creando la variable de iniciación
app = Flask(__name__)

# Definiendo rutas
@app.route('/')
def index():
    return 'Hola Mundo'
