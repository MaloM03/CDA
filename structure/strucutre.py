import mysql.connector
import os
import getpass

# RECUPERATION VAR ENV
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_NAME = os.getenv('DB_NAME')
TABLE_NAME = os.getenv('TABLE_NAME')

#====================================================
  
def connect_to_database(host, user, password, database):
    global g_mydb
    try:
        g_mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Connexion réussie à la base de données.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de la connexion : {err}")
        return False
    finally:
        return True

def display_table(table_name):
    try:
        cursor = g_mydb.cursor()
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except mysql.connector.Error as err:
        print(f"Erreur lors de la récupération des données : {err}")
    finally:
        if cursor:
            cursor.close()

#====================================================

if __name__=="__main__":
    password = getpass.getpass("Attente mot de passe de la BDD : ")
    if connect_to_database(DB_HOST, DB_USER, password, DB_NAME):
        display_table(TABLE_NAME)
    else:
        print("erreur de connexion")