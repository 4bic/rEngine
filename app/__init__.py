from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# local imports
import config
from config import app_config
# import models

# from models import User, Results

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
        return '<E-mail %r>' % self.email

class Results(db.Model):
    __tablename__ = "keywords"
    id = db.Column(db.Integer(),primary_key=True)
    user_name = db.Column(db.String())
    text = db.Column(db.String())
    user_created = db.Column(db.String())

    def __init__(self, name,text,created):
        self.name = user_name
        self.text = text
        self.created = user_created

    def __repr__(self):
        return '<E-mail %r>' % self.email

# Set "homepage" to index.html
@app.route('/')

# def index():
#     return render_template('index.html')
def index():
    return render_template('wordy.html')

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

if __name__ == '__main__':
    #app.debug = True
    app.run()
