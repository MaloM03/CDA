import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mysql.connector

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'uimm'    
DB_NAME = 'test_db'
TABLE_NAME = 'client'

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
        server.starttls()  # Activer TLS
        
        print("Connexion avec les identifiants...")
        server.login(sender_email, app_password)
        
        print("Envoi de l'email...")
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email envoyé avec succès !")
    
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")
    
    finally:
        server.quit()  # Fermer la connexion

def connect_to_database(host, user, password, database):
    """
    Établit une connexion à une base de données MySQL.

    :param host: Adresse du serveur MySQL.
    :param user: Nom d'utilisateur MySQL.
    :param password: Mot de passe MySQL.
    :param database: Nom de la base de données.
    :return: Objet de connexion MySQL ou None en cas d'erreur.
    """
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
    
def return_table_data(connection, table_name):
    """
    Récupère les données d'une table.
    """
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


def add_client(connection, nom, numero, ville, code_postal, adresse):
    """
    Ajoute un nouveau client à la base de données.
    
    :param connection: L'objet de connexion MySQL.
    :param nom: Le nom du client.
    :param numero: Le numéro de téléphone du client.
    :param ville: La ville du client.
    :param code_postal: Le code postal du client.
    :param adresse: L'adresse du client.
    """
    try:
        cursor = connection.cursor()

        # Requête SQL pour insérer un nouveau client
        query = """
        INSERT INTO client (nom, numéro, ville, code_postal, adresse) 
        VALUES (%s, %s, %s, %s, %s)
        """
        # Exécution de la requête avec les valeurs
        cursor.execute(query, (nom, numero, ville, code_postal, adresse))
        
        # Valider l'insertion dans la base de données
        connection.commit()

        print("Client ajouté avec succès.")
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'ajout du client : {err}")
    finally:
        if cursor:
            cursor.close()
