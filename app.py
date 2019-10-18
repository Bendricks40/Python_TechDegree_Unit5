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
    entries = models.Entries.select()
    return render_template('index.html', entries=entries)


@app.route('/new', methods=('GET', 'POST'))
def create():
    form = forms.JournalEntry()
    if form.validate_on_submit():
        models.Entries.create_entry(
            title=form.title.data,
            dateCreated=form.dateCreated.data,
            timeSpent=form.timeSpent.data,
            learned=form.learned.data,
            resources=form.resources.data
        )
        return redirect(url_for('index'))
    return render_template('new.html', form=form)


@app.route('/entries/<int:entry_id>')
def details(entry_id):
    entry = models.Entries.select().where(models.Entries.id==entry_id)
    return render_template('detail.html', entry=entry)


@app.route('/entries/<id>/edit')
def edit():
    return "This is where you edit an entry by it's ID"


@app.route('/entries/<id>/delete')
def delete():
    return "This is the entries/<id>/delete page where you would be deleting a specific entry"


if __name__ == '__main__':
    models.initialize()

app.run(debug=DEBUG, host=HOST, port=PORT)
