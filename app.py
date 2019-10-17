from flask import (Flask, g, render_template, flash, redirect, url_for)
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import check_password_hash
from wtforms.fields.html5 import DateField

import forms
import models


DEBUG = True
PORT = 8080
HOST = '0.0.0.0'


app = Flask(__name__)
app.secret_key = 'djkc8@mndp40t*B)*#&$@dmf>#<#<?#<>s.D>Sfaezi'


@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    print('connected to database!')
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database after each request"""
    g.db.close()
    print('closed database!')
    return response


@app.route('/')
@app.route('/entries')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/new', methods=('GET', 'POST'))
def create():
    print("im in the create function")
    form = forms.JournalEntry()
    print("about to do the if statement")
    print(form.title.data)
    print("here are results of the validate on submit check: " + str(form.validate_on_submit()))
    if form.is_submitted():
        print("submitted")
    if form.validate():
        print("valid")
    if form.validate_on_submit():
        print("the form was validated successfully")
        print("Title: " + form.title.data)
        print(form.dateCreated.data)
        print("Time Spend: " + form.timeSpent.data)
        print("Learned: " + form.learned.data)
        print("resources: " + form.resources.data)
        models.Entries.create_entry(
            title=form.title.data,
            dateCreated=form.dateCreated.data,
            timeSpent=form.timeSpent.data,
            learned=form.learned.data,
            resources=form.resources.data
        )
        return redirect(url_for('index'))
    return render_template('new.html', form=form)


@app.route('/entries/<id>')
def details():
    return "This is the entries page where you view a specific entry by it's id"


@app.route('/entries/<id>/edit')
def edit():
    return "This is where you edit an entry by it's ID"


@app.route('/entries/<id>/delete')
def delete():
    return "This is the entries/<id>/delete page where you would be deleting a specific entry"


if __name__ == '__main__':
    models.initialize()

app.run(debug=DEBUG, host=HOST, port=PORT)
