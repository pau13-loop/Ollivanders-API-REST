# Flask and Flask things
from flask import Flask, request, redirect, render_template, url_for, session, flash
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import (
    InputRequired,
    Email,
    Length,
    DataRequired,
    EqualTo,
    ValidationError,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)

# Flask RESTful
from flask_restful import Resource, Api

# Importamos CORS
from flask_cors import CORS

# Import Resources
from resources.resources_sql.wellcome import Wellcome
from resources.resources_sql.inventario import Inventario
from resources.resources_sql.updateQuality import UpdateQuality
from resources.resources_sql.items import Items
from resources.resources_sql.quality import Quality
from resources.resources_sql.sellin import Sellin

# Import from Repository the db_connection.py
from repository.repository_sql import db_connection

# Import Users Model SQLAlchemy
from repository.repository_sql.models.users import User

# SERVICES Methods to help us with Users, Login and Register
from service.service_sql.service import Service


app = Flask(__name__)
# secret key
app.secret_key = "secretkey"

CORS(app)

if app.config["ENV"] == "production":
    # Configuration APP Flask Production
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    # Configuration APP Flask Testing
    app.config.from_object("config.TestingConfig")
else:
    # Configuration APP Flask Development
    app.config.from_object("config.DevelopmentConfig")

# Init the Flask APP
db_connection.init_app(app)

# *****************************************
# * API SECTION

# API REST to be able to test
api = Api(app, catch_all_404s=True)

# Add Resources
# api.add_resource(Wellcome, '/')
api.add_resource(Inventario, "/inventory")
# GET item by name: '/items/name/<string:item_name>'
# POST, DELETE: '/items'
api.add_resource(
    Items, "/items/name/<string:item_name>", "/items", "/items/id/<int:id_item>/"
)
api.add_resource(Sellin, "/items/sellin/<int:item_sell_in>")
api.add_resource(Quality, "/items/quality/<int:item_quality>")
api.add_resource(UpdateQuality, "/update_quality")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
