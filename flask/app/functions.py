import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mysql.connector
from datetime import datetime

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'uimm'    
DB_NAME = 'test_db'
TABLE_NAME = 'membres'

def envoyer_email(sender_email, receiver_email, subject, body, app_password):
    print("Création de l'email...")
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        print("Connexion au serveur SMTP...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        print("Connexion avec les identifiants...")
        server.login(sender_email, app_password)
        
        print("Envoi de l'email...")
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email envoyé avec succès !")
    
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")
    
    finally:
        server.quit()

def connect_to_database(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Connexion réussie à la base de données.")
        return connection
    except mysql.connector.Error as err:
        print(f"Erreur lors de la connexion : {err}")
        return None
    
def return_member(connection, table_name):
    if connection is None:
        print("Pas de connexion à la base de données.")
        return []

    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as err:
        print(f"Erreur lors de la récupération des données : {err}")
        return []
    finally:
        if cursor:
            cursor.close()


def add_member(connection, username, password, email, joueur_pref):
    try:
        cursor = connection.cursor()

        date_creation = datetime.now()

        query = """
        INSERT INTO membres (username, password, email, date_creation, joueur_pref) 
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (username, password, email, date_creation, joueur_pref))
        connection.commit()

        print("Membre ajouté avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'ajout du membre : {err}")
    finally:
        if cursor:
            cursor.close()

def get_user(connection, username, password):
    try:
        cursor = connection.cursor(dictionary=True)
        
        query = """
        SELECT * FROM membres WHERE username = %s AND password = %s
        """
        cursor.execute(query, (username, password))
        
        user = cursor.fetchone()
        if user:
            return user
        else:
            return None

    except mysql.connector.Error as err:
        print(f"Erreur lors de la récupération de l'utilisateur : {err}")
        return None
    finally:
        if cursor:
            cursor.close()
