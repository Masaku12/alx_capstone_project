# Imports Flask and SQLAlchemy modules
from flask_sqlalchemy import SQLAlchemy

# Creates an instance of the SQLAlchemy class
db = SQLAlchemy()

# Defines a User model for user-related data
class User(db.Model):
    # Defines the User model's fields and data types
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)

# Defines a Recipe model for recipe-related data
class Recipe(db.Model):
    # Defines the Recipe model's fields and data types
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    ingredients = db.Column(db.Text)
    instructions = db.Column(db.Text)
    cuisine = db.Column(db.String(100))
    cooking_time = db.Column(db.String(100))
    servings = db.Column(db.String(100))

# Defines a FavoriteRecipe model to represent users' favorite recipes
class FavoriteRecipe(db.Model):
    # Defines the FavoriteRecipe model's fields
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

# Defines a Review model for user reviews of recipes
class Review(db.Model):
    # Defines the Review model's fields
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    rating = db.Column(db.Integer)
    review_text = db.Column(db.Text)

# These models will create and manage the database tables
# associated with users, recipes, favorites, and reviews.

