from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_table import Table, Col
import psycopg2

# local imports
import config
from config import app_config
# import models , routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name,email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Keyword(db.Model):
    __tablename__ = "keywords"
    id = db.Column(db.Integer, primary_key=True)
    search_term = db.Column(db.String, nullable=False)

    def __init__(self, search_term):
        self.search_term = search_term

    def __repr__(self):
        return '<search_term {}'.format(self.name)

class Results(Table):
    text = Col('text', show=False)
    user_name = Col('user_name')
    user_location = Col('user_location')

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

# @app.route('/keywords')
# def word_entry():
#     return render_template('wordy.html')

@app.route('/word_search', methods=['Get','POST'])
def word_search():
    search_term = None
    if request.method == 'POST':
        search_term = request.form['search_term']
        if not db.session.query(Keyword).filter(Keyword.search_term == search_term).count():
            reg = Keyword(search_term)
            db.session.add(reg)
            db.session.commit()
        # return render_template('results.html')
    return render_template('wordy.html')

@app.route('/results',)
def search_results():
    results = Keyword.query.all()

    return render_template('results.html', results=results)

if __name__ == '__main__':
    #app.debug = True
    app.run()
