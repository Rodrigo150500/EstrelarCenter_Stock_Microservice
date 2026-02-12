import pytest

from dotenv import load_dotenv
load_dotenv("dev.env")

from src.model.mongo.settings.mongo_db_connection import mongo_db_connection
from src.model.mongo.repository.product_repository import ProductRepositoryMongo
from src.use_case.mongo.remove_item_use_case import RemoveItemMongoUseCase

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

from src.errors.types.http_not_found import HttpNotFound

from remove_item_use_case_integration_data import setup_use_case_data, remove_variant_succesfully_data

mongo_db_connection.connect()

@pytest.fixture
def setup_use_case():

    data = setup_use_case_data()

    try:

        connection = mongo_db_connection.get_db_connection()
        repository = ProductRepositoryMongo(connection)
        use_case = RemoveItemMongoUseCase(repository)

        repository.insert_product(data["product"])

        object_id_1 = repository.get_product_by_code(data["product"]["code"])["variants"][0]["_id"]
        object_id_2 = repository.get_product_by_code(data["product"]["code"])["variants"][1]["_id"]

        yield object_id_1, object_id_2, repository, use_case
    
    finally:
        
        repository.delete_product_by_code(data["product"]["code"])


def test_remove_variant_succesfully(setup_use_case):

    object_id_1, object_id_2, repository, use_case = setup_use_case

    data = remove_variant_succesfully_data(object_id_1)

    http_request = HttpRequest(params=data["params"])

    response = use_case.handle(http_request)

    assert isinstance(response, HttpResponse)

    code = data["params"]["code"]

    obj_1_is_in_database = repository.check_if_variant_exists(code, object_id_1)
    obj_2_is_in_database = repository.check_if_variant_exists(code, object_id_2)

    assert obj_1_is_in_database == False
    assert obj_2_is_in_database == True


def test_remove_variant_that_not_exists(setup_use_case):

    object_id_1, object_id_2, repository, use_case = setup_use_case

    params = {"code": "10", "_id": "68b70ef826423e500863c1c7"}

    http_request = HttpRequest(params=params)

    with pytest.raises(HttpNotFound):
        use_case.handle(http_request)

    obj_1_is_in_database = repository.check_if_variant_exists("10", object_id_1)
    obj_2_is_in_database = repository.check_if_variant_exists("10", object_id_2)

    assert obj_1_is_in_database == True
    assert obj_2_is_in_database == True




