from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = '73ac57d0ad7b1a5f49ee87c492ff12fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['BASIC_AUTH_USERNAME'] = 'james'
app.config['BASIC_AUTH_PASSWORD'] = 'agent'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
basic_auth = BasicAuth(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from navenio import routes