import flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = flask.Flask(__name__)
app.config['SECRET_KEY'] = '@108#2022T@f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/data.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from logs.routes import routes
