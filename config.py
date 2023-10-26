from flask_sqlalchemy import SQLAlchemy
from flask import app
import requests

# Configures the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

# Initializes the SQLAlchemy with the Flask App
db = SQLAlchemy(app) 
