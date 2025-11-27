import os
import firebase_admin
from firebase_admin import credentials, db


DATABASE_URL = os.getenv("DATABASE_URL")


class FirebaseDBConnection:

    def __init__(self):
    
        self.__credentials = credentials.Certificate(os.path.abspath(
                    os.path.join(os.path.dirname(__file__), "keys/firebase_key.json")
                ))
    def connect(self):

        firebase_admin.initialize_app(self.__credentials,{
            "databaseURL":DATABASE_URL
        })
    
    def get_connection(self):

        return db

firebase_db_connection = FirebaseDBConnection()


