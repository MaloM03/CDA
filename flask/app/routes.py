from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index')
def index():
    srtResult='ATTENTION TEST'
    return srtResult
