from dotenv import load_dotenv
load_dotenv("dev.env")

import pytest

from src.model.firebase.settings.firebase_db_connection import firebase_db_connection
from src.model.firebase.repository.product_repository import ProductRepositoryFirebase
from src.use_case.firebase.insert_product_use_case import InsertProductFirebaseUseCase

from .data.insert_product_use_case_integration_data import insert_product_sucessfully_data, insert_product_invalid_body_data

from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

@pytest.fixture
def setup_use_case():

    firebase_db_connection.connect()

    connection = firebase_db_connection.get_connection()
    repository = ProductRepositoryFirebase(connection)
    use_case = InsertProductFirebaseUseCase(repository)

    return use_case


@pytest.mark.skip()
def test_insert_product_sucessfully(setup_use_case):

    use_case = setup_use_case

    data = insert_product_sucessfully_data()

    body = data["body"]

    http_request = HttpRequest(body=body)

    response = use_case.handle(http_request)

    assert response.status_code == 201
    assert response.body == data["expected_response"]


@pytest.mark.skip()
def test_insert_product_invalid_body(setup_use_case):

    use_case = setup_use_case

    data = insert_product_invalid_body_data()

    body = data["body"]

    http_request = HttpRequest(body=body)

    with pytest.raises(HttpUnprocessableEntity):
        use_case.handle(http_request)








