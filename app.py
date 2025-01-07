from flask import Flask, render_template, request, redirect, url_for, session, flash
import secrets
app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/packages')
def packages():
    return render_template('packages.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/destination')
def destinations():
    return render_template('destination.html')

if __name__ == '__main__':
    app.run(debug=True)