from flask import Flask
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
# from repository.db_mock import db_connection_mock
from repository.repository_sql import db_connection


def create_app():

    app = Flask(__name__)

    CORS(app)

    app.config["ENV"] = "test"
    app.config["TESTING"] = True

    # Init the Flask APP
    # db_connection_mock.init_app(app)
    # Debido a que el APP Flask ya tiene el "Environment"
    db_connection.init_app(app)

    # API REST to be able to test
    api = Api(app, catch_all_404s=True)

    # Add Resources
    api.add_resource(Wellcome, "/")
    api.add_resource(Inventario, "/inventory")
    # GET item by name: '/items/name/<string:item_name>'
    # POST, DELETE: '/items'
    api.add_resource(
        Items, "/items/name/<string:item_name>", "/items", "/items/id/<int:id_item>/"
    )
    api.add_resource(Sellin, "/items/sellin/<int:item_sell_in>")
    api.add_resource(Quality, "/items/quality/<int:item_quality>")
    api.add_resource(UpdateQuality, "/update_quality")

    return app


if __name__ == "__main__":
    app = create_app()
    print(app.config["SQLALCHEMY_DATABASE_URI"])
    app.run(host="0.0.0.0", port=5000, debug=True)
