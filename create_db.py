from app import app, db

# Establecer el contexto de la aplicación
with app.app_context():
    db.create_all()
    print("Base de datos creada exitosamente")
