Creacion de BD para flask en contenedor de postgres ya existente


# 1. Encuentra el nombre de tu contenedor (ej: 'mi-proyecto-db-1')
docker ps

# 2. Entra al contenedor con psql
# Usa el usuario que tienes en tu .env (ej: 'django_user')
docker exec -it 70a179550fa8 psql -U django_user -d djangodb


# 3. Una vez dentro de psql (verás postgres=# o djangodb=#), crea la nueva base de datos:

CREATE DATABASE blogposts_db;

# 4. Sales con \q


Aclarar que el usuario y contraseña de postgress es para todas las aplicaciones la misma, lo único que cambiaria es la bd.

El yml del contenedor de postgres tiene la instruccion de construir la primera bd del contenedor pero es de otra aplicación.
Es por ello que hay que meterse ene l contenedor a mano y crear la bd a mano sin tener que meterlo en en .ev de postgres ni en el yml.Unicamente hay que meter los datos del usuario y contraseña compartido y la bd nueva en el archivo de configuracion de la aplicación de flask.




# Anulacion de registro de usuarios nuevos:
## Comentar las siguientes lineas de los siguientes archivos.
login.html
 ``` <!--             <a href="{{ url_for('auth.register') }}">Crear cuenta</a> -->  ```

index.html
 ``` <!--                <a href="{{url_for('auth.register') }}" class="btn btn-outline-dark w-50 fs-3">Registrate</a> -->  ```

base.html
 ``` <!--                   <a href="{{url_for('auth.register') }}" class="btn btn-warning">Registrate</a>        -->  ```


## Comentar funcion register en auth.py
 ```
# COMENTADO TODA LA FUNCION PARA ELIMINAR LA OPCION DE REGISTRARSE Y EVITAR PROBLEMAS DE SEGURIDAD
# @bp.route('/register', methods=('GET', 'POST'))
# def register():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         email = request.form.get('email')
#         password = request.form.get('password')
        
#         user = User(username, email, generate_password_hash(password))
        
#         # Validación básica
#         error = None
#         user_email = User.query.filter_by(email=email).first()
        
#         if user_email is None:
#             db.session.add(user)
#             db.session.commit()
#             return redirect(url_for('auth.login'))
#         else:
#             error = f'El correo {email} ya está registrado'
        
#         flash(error)
        
#     return render_template('auth/register.html')

 ```