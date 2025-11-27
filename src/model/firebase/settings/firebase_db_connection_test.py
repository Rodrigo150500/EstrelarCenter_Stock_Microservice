import pytest
from dotenv import load_dotenv
load_dotenv("dev.env")
from firebase_admin import db
from .firebase_db_connection import FirebaseDBConnection

@pytest.mark.skip()
def test_connection_firebase_sucessfully():

    firebase_connection = FirebaseDBConnection()

    firebase_connection.connect()

    ref = db.reference("/")

    data = ref.get()

    assert data is not None