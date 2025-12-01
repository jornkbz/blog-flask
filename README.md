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