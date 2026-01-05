import pytest

from dotenv import load_dotenv
load_dotenv("dev.env")

from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.get_image_use_case import GetImageMongoUseCase

from get_image_use_case_integration_data import get_image_sucessfully, get_image_not_found, setup_use_case_data

from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_not_found import HttpNotFound

@pytest.fixture
def setup_use_case():

    data = setup_use_case_data()
    
    code = data["product"]["code"]

    mongo_db_connection.connect()

    connection = mongo_db_connection.get_db_connection()
    repository = ProductRepositoryMongo(connection)
    use_case = GetImageMongoUseCase(repository)

    try:
        repository.insert_product(data["product"])

        object_id = str(repository.get_product_by_code(data["product"]["code"])["variants"][0]["_id"])

        yield use_case, code, object_id

        repository.delete_product_by_code(data["product"]["code"])

    finally:

        repository.delete_product_by_code(data["product"]["code"])


def test_get_image_sucessfully(setup_use_case):

    use_case, code, object_id = setup_use_case
    
    data = get_image_sucessfully(code, object_id)

    http_request = HttpRequest(params=data["params"])

    response = use_case.handle(http_request)

    assert response.body == data["expected_response"]
    assert response.status_code == 200


def test_get_image_not_found(setup_use_case):

    use_case, _, _ = setup_use_case
    
    data = get_image_not_found()

    http_request = HttpRequest(params=data["params"])

    with pytest.raises(HttpNotFound):
        use_case.handle(http_request)   

    