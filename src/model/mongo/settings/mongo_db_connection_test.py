from dotenv import load_dotenv
load_dotenv("dev.env")

from .mongo_db_connection import mongo_db_connection
from pymongo.errors import ConnectionFailure

def test_connection():


    try:
        mongo_db_connection.connect()

        connection = mongo_db_connection.get_db_connection()

        connection.command("ping")
        print("Health check: OK")
        

    except ConnectionFailure:
        print("Health check: Falhou")

