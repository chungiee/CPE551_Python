"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/documents')
def documents():
    """Renders the documents page."""
    return render_template(
        'documents.html',
        title='Documents',
        year=datetime.now().year,
        message1='Select multiple documents to upload.',
        message2='Uploaded Documents:'
   )

@app.route('/photos')
def photos():
    """Renders the about page."""
    return render_template(
        'photos.html',
        title='Photos',
        year=datetime.now().year,
        message1='Python Flask Upload Multiple Images theme.',
        message2='Select multiple images to upload.',
        message3='Uploaded photos:'
    )

@app.route('/uploads')
def uploads():
    return render_template(
        'uploads.html',
        title="Uploads",
        year=datetime.now().year,
        message1 = 'Uploaded Documents:'
        )




