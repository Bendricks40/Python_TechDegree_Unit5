from flask import (Flask, g, render_template, flash, redirect, url_for)
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash


DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'djkc8@mndp40t*B)*#&$@dmf>#<#<?#<>s.D>Sfaezi'


@app.route('/')
@app.route('/entries')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/new')
@app.route('/entries/new')
def create():
    return render_template('new.html')


@app.route('/entries/<id>')
def details():
    return "This is the entries page where you view a specific entry by it's id"


@app.route('/entries/<id>/edit')
def edit():
    return "This is where you edit an entry by it's ID"


@app.route('/entries/<id>/delete')
def delete():
    return "This is the entries/<id>/delete page where you would be deleting a specific entry"


app.run(debug=DEBUG, host=HOST, port=PORT)
