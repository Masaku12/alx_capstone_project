from flask import Flask, render_template, request, jsonify
from models import db, User, Recipe, FavoriteRecipe, Review
from flask_sqlalchemy import SQLAlchemy
import requests

# Creates a Flask application
app = Flask(__name__)

# Route for index
@app.route('/')
def index():
    return render_template('home.html')

# a route for the home
@app.route('/home')
def home():
    return render_template('home.html')

# Route for the search
@app.route('/search')
def search():
    return render_template('search.html')

# Route for results
@app.route('/results')
def result():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
