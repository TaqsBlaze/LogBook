from http import client
from msilib.schema import Error
from flask import redirect, render_template, request, url_for, flash
from cryptography.fernet import Fernet
import flask_login
from logs.forms.forms import *
from logs.models.models import User, Entry
from logs import app,db
from flask_login import login_user, current_user



@app.route("/", methods = ['GET','POST'])
def login():
    
    form = LoginForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            
            user = User.query.filter_by(username = form.username.data).first()
            if user != None:
                login_user(user)
                flash(f"Logged in as {user.fname} {user.lname}", 'success')
                return redirect(url_for("logging"))
            else:
                flash("Unable to login!",'danger')
                return redirect(url_for("login"))        
        
    return render_template(['login.html','index.html'], title="Login", form=form)



@app.route("/register", methods = ['GET','POST'])
def register():
    
    
    form = SignupForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(
                username = form.username.data,
                fname = form.fname.data,
                lname = form.lname.data,
                email = form.email.data,
                phone = form.phone.data,
                password = form.password.data,
            )
            
            try:
                db.session.add(user)
                db.session.commit()
                flash("Account created successfully you can now login","success")
                return redirect(url_for("login"))
            except Exception as Error:
                flash(f"{Error}")
                return redirect(url_for("register"))
        
    return render_template(['register.html','signup.html'], title="Register new user", form = form)


@app.route("/log", methods = ['GET','POST'])
def logging():
    
    form = LogForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            log = Entry(
                client = form.client.data,
                company = form.company.data,
                contact = form.contact.data,
                email = form.email.data,
                query = form.query.data,
                description = form.description.data,
                user_id = current_user.id
            )
            
            try:
                db.session.add(log)
                db.session.commit()
                flash("Query has been logged","success")
                return redirect(url_for("logging"))
            except Exception as Error:
                flash("Something went wrong!","danger")
                flash(f"{Error}","danger")
                return redirect(url_for("logging"))
            
        else:
            
            flash("Query could not be logged", "danger")
            return url_for("logging")
        
    return render_template(['index.html','logging.html'], title="Log", form = form)


@app.route("/logged", methods = ['GET','POST'])
def logged():
    
    logs = Entry.query.all()
    search = SearchForm()
    
    if request.method == 'POST':
        if search.validate_on_submit():
            logs = Entry.query.filter_by(ref = search.iterm.data).all()
            
            if logs != None or len(logs) > 0:
                logs = logs
                
    return render_template(['logged.html'], title = "Logged", logs=logs)

