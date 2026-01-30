from flask_cors import CORS

from flask import Flask
from flasgger import Swagger

from src.main.routes.product_routes import product_routes_bp

from src.model.mongo.settings.mongo_db_connection import mongo_db_connection

mongo_db_connection.connect()

def create_app() -> Flask:

    app = Flask(__name__)

    CORS(app)

    app.register_blueprint(product_routes_bp)

    Swagger(app)

    return app