from app import app
from flask import render_template, redirect, request
from app.forms import ConfigForm

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
        return render_template('retour.html')
    else:
        return "Veuillez remplir tous les champs."