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

@app.route('/myformC')
def myformC():
    return render_template('formC.html')

@app.route('/index')
def index():
    srtResult='ATTENTION TEST'
    return srtResult

@app.route('/retour', methods=['POST'])
def submit():
    name = request.form['name']
    password = request.form['password']
    email = request.form['email']
    joueurpref = request.form['joueurpref']
    
    if name and email:
        expediteur = "remelifanpage@gmail.com"
        destinataire = email
        objet = "Inscription FAN PAGE DE TENNIS"
        corps = f"Bienvenue {name} sur la page Remeli Tennis Fan"
        mot_de_passe_app = "jcnp oerh hygf hfkl"
        connection = connect_to_database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        add_member(connection, name, password, email, joueurpref)
        return render_template('retour.html', name=name, email=email)
        
    else:
        return "Veuillez remplir tous les champs."

@app.route('/retourC', methods=['POST'])
def submitC():
    username = request.form['name']
    password = request.form['password']
    
    if username and password:
        connection = connect_to_database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
        resultat = get_user(connection, username, password)
        if resultat:
            print("vu mon gars")
        else:
            print("pas vu mon gars")
        return render_template('retour.html', name=username, email=password)
        
    else:
        return "Veuillez remplir tous les champs."
    
@app.route('/refresh', methods=['POST'])
def refresh():
    print("Le bouton a été cliqué et le message est imprimé dans la console !")

    return render_template('form.html')

@app.route('/mydata')
def mydata():
    connection = connect_to_database(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    data = return_member(connection, TABLE_NAME)
    return render_template('mydata.html', data=data)