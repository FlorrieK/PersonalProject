from flask import Flask, render_template, url_for, flash, redirect
from datetime import datetime
import helper
from dictionary import *
from forms import LoginForm, RegistrationForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')

@app.route('/indexgallery')
def home():
    return render_template('indexgallery.html')

@app.route('/about')
def about ():
    return render_template('about.html')


if __name__ == '__name__':
    app.run(debug = True)


#to initialize an instance of the database
db = SQLAlchemy(app)

class User(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    #type string with character max 50; is unique; is required
    email = db.Column(db.String(50), unique = True, nullable = False)
    #type string with character max 50; is unique; is required
    password = db.Column(db.String(50), nullable = False)
    #size of string is determined by the hashing algorithm, so every password will be 50 characters  long
    account = db.relationship('Account', backref = 'username')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

@app.route('/home')
def home():

    return render_template('home.html', title = 'Home')

@app.route("/registration", methods = ['GET', 'POST'])
def register():

    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('timeDisplay'))
    return render_template('registration.html', title = 'Registration', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "bob@bob.bob" or form.username.data == "bobbob" and form.password.data == "bob123456":
            flash('Congrats on your success logging in. We continue to be proud of you.', 'success')
            return redirect(url_for('timeDisplay'))
        else:
            flash('Oops, looks like somebody is a failure. I am pretty disappointed, but if you still believe in yourself, you can try typing in your username/email and password again.')


    return render_template('login.html', title = 'Login', form = form)

@app.route('/abouttheartist', methods = ['GET', 'POST'])
def abouttheartist():

    return render_template('abouttheartist.html', title = 'About the Artist', form = form)

@app.route('/aboutthewebdesigner', methods = ['GET', 'POST'])
def abouttheartist():

    return render_template('aboutthewebdesigner.html', title = 'About the Web Designer', form = form)

if __name__ == '__name__':
    app.run(debug = True)

    # $env:FLASK_ENV = "development"


    # $env:FLASK_ENV = "development"
