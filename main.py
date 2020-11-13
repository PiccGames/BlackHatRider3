from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from flask import session
import bcrypt

app = Flask(__name__)
app.secret_key = 'bhrtwoandonewerewimpy'

users     = ['a@a']
passwords = ['a']
user_info = {
    'bio': 'This is a completely random biography'
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/profile/<username>')
def prfile_page(username):
    if username in user_info:
        return render_template('profile.html', user=username, bio=user_info[username], has_bio=True)
    else:
        return render_template('profile.html', user=username, has_bio=False)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    _user = request.form['email']
    _pass = request.form['password']
    
    username = (_user in users)
    password = (_pass in passwords)

    if username and password:
        session['loggedIn'] = True
        return redirect(url_for('game'))
    else:
        session['loggedIn'] = False
        return redirect(url_for('home'))

@app.route('/game')
def game():
    if session['loggedIn']:
        return render_template('game.html')
    else:
        return redirect(url_for('home'))