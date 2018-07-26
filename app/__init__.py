from flask import Flask, render_template, request, jsonify, session, redirect, url_for, json
from flask_table import Table, Col
import psycopg2
import os

# local imports
import config
from config import app_config
from .models import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # landing page
# @app.route('/')
# def landing():
#     return render_template('base.html')

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

# Save name & e-mail to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
    name = None
    email = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(name,email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')

@app.route('/keywords')
def word_entry():
    return render_template('new.html')

@app.route('/word_search', methods=['GET','POST'])
def word_search():
    search_term = None
    tweets = Results.query.filter(Results.predictions =='fashion').all()
    if request.method == 'POST':
        search_term = request.form['search_term']
        if not db.session.query(Keyword).filter(Keyword.search_term == search_term).count():
            reg = Keyword(search_term)
            db.session.add(reg)
            db.session.commit()
        return redirect(url_for('word_search'))

    return render_template('wordy.html',tweets=tweets)

@app.route('/results/<int:page_num>')
def tweet_result(page_num):
    tweets = Results.query.paginate(per_page=6,page=page_num,error_out=True)
    return render_template('results.html',tweets=tweets)

# tests on displaying data
@app.route('/basic')
def basic_page():
    tweets = Results.query.filter(Results.predictions =='fashion').all()
    return render_template('basic.html',tweets=tweets)


if __name__ == '__main__':
    app.debug = True
    app.run()
