from flask import (Flask, g, render_template, redirect, url_for, request)


import forms
import models


DEBUG = True
PORT = 8080
HOST = '0.0.0.0'


app = Flask(__name__)
app.secret_key = 'djkc8@mndp40t*B)>s.D>Sfaezi'


@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database after each request"""
    g.db.close()
    return response


@app.route('/')
@app.route('/entries')
@app.route('/index.html')
def index():
    """Load the "home" page with all entries"""
    entries = models.Entries.select()
    return render_template('index.html', entries=entries)


@app.route('/new', methods=('GET', 'POST'))
def create():
    """Makes a new Journal Entry"""
    form = forms.JournalEntry()
    if form.validate_on_submit():
        models.Entries.create_entry(
            title=form.title.data,
            datecreated=form.dateCreated.data,
            timespent=form.timeSpent.data,
            learned=form.learned.data,
            resources=form.resources.data
        )
        return redirect(url_for('index'))
    return render_template('new.html', form=form)


@app.route('/entries/<int:entry_id>')
def details(entry_id):
    """Displays the details of a specific Journal entry per the passed in ID"""
    entry = models.Entries.select().where(models.Entries.id == entry_id)
    return render_template('detail.html', entry=entry)


@app.route('/entries/<int:entry_id>/delete')
def delete(entry_id):
    """Deletes the specified Journal entry by its ID"""
    models.Entries.delete().where(models.Entries.id == entry_id).execute()
    print("just deleted it, now redirecting back to index")
    return redirect(url_for('index'))


@app.route('/entries/<int:entry_id>/edit',  methods=('GET', 'POST'))
def edit(entry_id):
    """Passed the chosen entry to the edit page so a user can make edits or delete the entry"""
    entry = models.Entries.get_or_none(models.Entries.id == entry_id)
    form = forms.JournalEntry(obj=entry)
    if request.method == 'POST':
        print("Form has been posted!")
        print(entry_id)
        print(form.title.data)
    if form.validate_on_submit():
        models.Entries.update(
            title=form.title.data,
            dateCreated=form.dateCreated.data,
            timeSpent=form.timeSpent.data,
            learned=form.learned.data,
            resources=form.resources.data
        ).where(models.Entries.id == entry_id).execute()
        return redirect(url_for('index'))
    return render_template('edit.html', entry=entry, form=form)


if __name__ == '__main__':
    models.initialize()

app.run(debug=DEBUG, host=HOST, port=PORT)
