from flask import Flask

app = Flask(__name__)

from app import routes
from app.C_MySqlBdd import MySqlBdd
import getpass

# CREATION OBJET BDD
bdd = MySqlBdd("python")
pwd = getpass.getpass("Entrer le mot de passe de la base de données : ")
connection = bdd.connect_to_database(pwd)


