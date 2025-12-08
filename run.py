from blogr import create_app

# --- CAMBIO AQUÍ ---
# Crea la app fuera del if para que sea accesible al importar
app = create_app()

if __name__ == '__main__':
    # Esto solo se usa si ejecutas "python run.py" manualmente
    app.run()