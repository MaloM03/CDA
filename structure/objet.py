import mysql.connector
import os
import getpass

# RECUPERATION VAR ENV
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_NAME = os.getenv('DB_NAME')
TABLE_NAME = os.getenv('TABLE_NAME')

#====================================================

class MySqlBdd:
    def __init__(self, user):
        self.user = user
        self.g_mydb = None

    def connect_to_database(self, password):
        try:
            self.g_mydb = mysql.connector.connect(
                host=DB_HOST,
                user=self.user,
                password=password,
                database=DB_NAME
            )
            print("Connexion réussie à la base de données.")
        except mysql.connector.Error as err:
            print(f"Erreur lors de la connexion : {err}")
            return False
        else:
            return True

    def display_table(self, table_name):
        try:
            cursor = self.g_mydb.cursor()
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

    def disconnect(self):
        self.g_mydb.close()

    def __del__(self):
        print("OBJET détruit")

#====================================================

if __name__=="__main__":

    password = getpass.getpass("Attente mot de passe de la BDD : ")

    MyDB = MySqlBdd("python")

    if MyDB.connect_to_database(password):
        MyDB.display_table(TABLE_NAME)
        MyDB.disconnect()
        del MyDB
    else:
        print("dommage")
    print("=============")

    