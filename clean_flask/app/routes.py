from app import app
from flask import render_template, redirect, request
from app.__init__ import bdd

@app.route('/')
def home():
    bdd.display_table("membres")
    print("do")
    return render_template('home.html')

@app.route('/membres')
def membres():
    data = bdd.return_member("membres")
    return render_template('membres.html', data=data)