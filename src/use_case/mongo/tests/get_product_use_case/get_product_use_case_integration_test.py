import pytest

from dotenv import load_dotenv
load_dotenv("dev.env")

from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.get_product_use_case import GetProductMongoUseCase

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from get_product_use_case_integration_data import get_product_sucessfully_data, get_product_not_found_data, setup_use_case_data

from src.errors.types.http_not_found import HttpNotFound

@pytest.fixture
def setup_use_case():

    try:

        data = setup_use_case_data()

        mongo_db_connection.connect()

        connection = mongo_db_connection.get_db_connection()
        repository = ProductRepositoryMongo(connection)
        use_case = GetProductMongoUseCase(repository)

        repository.insert_product(data["product"])

        object_id_1 = repository.get_product_by_code(data["product"]["code"])["variants"][0]["_id"]
        object_id_2 = repository.get_product_by_code(data["product"]["code"])["variants"][1]["_id"]
        
        yield object_id_1, object_id_2,repository, use_case
    
    finally:
        
        repository.delete_product_by_code(data['product']['code'])


def test_get_product_sucessfully(setup_use_case):

    object_id_1, object_id_2, repository, use_case = setup_use_case

    data = get_product_sucessfully_data(object_id_1, object_id_2)

    http_request = HttpRequest(params=data["params"])

    response = use_case.handle(http_request)

    isInDatabase = repository.check_if_product_exists(data["params"]["code"])

    assert isInDatabase == True

    assert isinstance(response, HttpResponse)

    assert response.body == data["expected_response"]



def test_get_product_not_found(setup_use_case):

    data = get_product_not_found_data()

    _, _, _, use_case = setup_use_case

    http_request = HttpRequest(params=data["params"])

    with pytest.raises(HttpNotFound):

        use_case.handle(http_request)

