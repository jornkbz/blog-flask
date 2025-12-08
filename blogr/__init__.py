from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Importamos locale aquí arriba para tenerlo ordenado
import locale 

db = SQLAlchemy()

def create_app():
    # Crear aplicación de flask
    app = Flask(__name__)
    
    app.config.from_object('config.Config')
    
    # Inicializar base de datos
    db.init_app(app)
    
    from flask_ckeditor import CKEditor
    ckeditor = CKEditor(app)
    
    # --- BLOQUE CORREGIDO PARA IDIOMA (WINDOWS + DOCKER) ---
    try:
        # Intenta primero el formato de Linux/Docker (es_ES.UTF-8)
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
        print("Locale configurado a es_ES.UTF-8 (Linux/Docker)")
    except locale.Error:
        try:
            # Si falla, intenta el formato de Windows (es_ES)
            locale.setlocale(locale.LC_ALL, 'es_ES')
            print("Locale configurado a es_ES (Windows)")
        except locale.Error:
            # Si todo falla, usa el por defecto y avisa
            print("Advertencia: No se pudo configurar el idioma español. Usando por defecto.")
    # -------------------------------------------------------
    
    # Registrar vistas
    from blogr import home
    app.register_blueprint(home.bp)
    
    from blogr import auth
    app.register_blueprint(auth.bp)
    
    from blogr import post
    app.register_blueprint(post.bp)

    from .models import User, Post
    
    with app.app_context():
        db.create_all()
        
    return app