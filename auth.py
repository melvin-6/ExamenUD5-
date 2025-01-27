# Importando Blueprint
from flask import Blueprint

# Creando instancia
bp = Blueprint('auth', __name__, url_prefix='/auth')

#Creado ruta y función
@bp.route('/register')
def register():
    return "Registrar usuario"

@bp.route('/login')
def login():
    return "Iniciar sesión
