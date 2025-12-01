import os
from dotenv import load_dotenv

# Carga las variables del archivo .env al entorno
load_dotenv()

class Config:
    # Usa os.getenv. El segundo parámetro es un valor por defecto (fallback)
    DEBUG = os.getenv('FLASK_DEBUG', '0') == '1'
    
    # Si no encuentra SECRET_KEY, usará 'dev' (solo para desarrollo local seguro)
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev')
    
    # Aquí capturamos la URL de la base de datos
    # Si no hay variable definida, podemos caer en SQLite por defecto para evitar errores
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///project.db')
    
    CKEDITOR_PKG_TYPE = 'full'