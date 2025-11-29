import pytest

from dotenv import load_dotenv
load_dotenv("dev.env")

from src.model.firebase.settings.firebase_db_connection import firebase_db_connection
from src.model.firebase.repository.product_repository import ProductRepositoryFirebase 
from src.use_case.firebase.delete_product_use_case import DeleteProductFirebaseUseCase

from src.main.http_types.http_request import HttpRequest

from src.errors.types.http_not_found import HttpNotFound
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity


@pytest.fixture
def setup_use_case():

    firebase_db_connection.connect()

    connection = firebase_db_connection.get_connection()
    repository = ProductRepositoryFirebase(connection)
    use_case = DeleteProductFirebaseUseCase(repository)

    return use_case

@pytest.mark.skip()
def test_delete_product_sucessfully(setup_use_case):

    use_case = setup_use_case

    http_request = HttpRequest(
        params={
            "code": "1"
        }
    )

    response = use_case.handle(http_request)

    assert response.body == {
        "data":{
            "operation":"delete",
            "count": 1,
            "attributes": {
                "code": "1"
            }
        }
    }

    assert response.status_code == 204
    

@pytest.mark.skip()
def test_delete_product_not_found(setup_use_case):

    use_case = setup_use_case

    http_request = HttpRequest(
        params={
            "code": "999999"
        }
    )

    with pytest.raises(HttpNotFound) as exc_info:
        use_case.handle(http_request)

    assert str(exc_info.value) == "Product not found"


@pytest.mark.skip()
def test_delete_product_invalid_params(setup_use_case):
    use_case = setup_use_case

    http_request = HttpRequest(
        params={
            # "code": "1"
        }
    )
    with pytest.raises(HttpUnprocessableEntity):
        use_case.handle(http_request) 