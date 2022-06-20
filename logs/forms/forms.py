from wtforms import *
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, Length
from flask_wtf import FlaskForm
#from logs.models.models import User




class LoginForm(FlaskForm):
    username = StringField("User name", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    login = SubmitField("Login")
    
    
    
    
class LogForm(FlaskForm):
    client = StringField("Client name", validators = [DataRequired()]) 
    company = StringField("Company name")
    contact = StringField("Contact number", validators = [DataRequired()])
    email = EmailField("Email")
    query = StringField("Query", validators = [DataRequired()])
    description = StringField("Description", validators = [DataRequired()])
    submit = SubmitField("Log")
    
class SignupForm(FlaskForm):
    fname = StringField("First name", validators = [DataRequired()])
    lname = StringField("Last name", validators = [DataRequired()])
    email = EmailField("Email", validators = [DataRequired()])
    username =StringField("Username", validators = [DataRequired()])
    phone = StringField("Phone number", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired(),Length(min = 6, max = 8, message = "Your password should be between 6 and 8 charactors long for more security")])
    confirmpassword = PasswordField("Confirm password", validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")
    
    def confirm(self):
        
        pass
    
    
    
class SearchForm(FlaskForm):
    
    iterm = StringField("Search", validators = [DataRequired()])
    pass