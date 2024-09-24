import os

# Récupérer la variable d'environnement USER_NAME
user_name = os.getenv('DB_PASSWORD')

if user_name:
    print(f"La variable d'environnement USER_NAME est : {user_name}")
else:
    print("La variable d'environnement USER_NAME n'est pas définie.")