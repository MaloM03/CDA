from app import app
from flask import render_template, redirect, request
from app.forms import ConfigForm
from app.functions import *

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/remeli')
def remeli():
    return render_template('remeli.html')

@app.route('/manarino')
def manarino():
    return render_template('manarino.html')

@app.route('/myform')
def myform():
    return render_template('form.html')

@app.route('/index')
def index():
    srtResult='ATTENTION TEST'
    return srtResult

@app.route('/retour', methods=['POST'])
def submit():
    # Récupérer les données du formulaire
    name = request.form['name']
    email = request.form['email']
    
    # Traitement des données (ex: validation)
    if name and email:
        expediteur = "remelifanpage@gmail.com"
        destinataire = email
        objet = "Inscription FAN PAGE DE TENNIS"
        corps = f"Bienvenue {name} sur la page Remeli Tennis Fan"
        mot_de_passe_app = "jcnp oerh hygf hfkl"
        connection = connect_to_database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        add_client(connection, name, 123123123, 'Rennes', 35000, email)
        envoyer_email(expediteur, destinataire, objet, corps, mot_de_passe_app)
        return render_template('retour.html', name=name, email=email)
        
    else:
        return "Veuillez remplir tous les champs."

@app.route('/refresh', methods=['POST'])
def refresh():
    print("Le bouton a été cliqué et le message est imprimé dans la console !")

    return render_template('form.html')

@app.route('/mydata')
def mydata():
    # Imprimer les données de la table
    connection = connect_to_database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    data = return_table_data(connection, TABLE_NAME)
    return render_template('mydata.html', data=data)