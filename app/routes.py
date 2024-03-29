from flask import Flask, render_template, url_for, flash, redirect
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post

posts = [
    

    {
        'author': 'Hans Seyle',
        'title' : 'Quote',
        'content': 'He who has conquered doubt and fear will conquer failure.',
        'date_posted': 'May 9, 2019'
    }
    
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register", methods = ['GET', 'POST'] )
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit() 
        flash('Your account has been created you can now log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', titile='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))    
    return render_template('login.html', title='Login', form=form)