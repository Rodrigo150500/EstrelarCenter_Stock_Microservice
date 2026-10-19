import pytest

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from src.validators.update_product_validator_request import update_product_validator_request

from src.utils.image_type import image_string

@pytest.fixture
def valid_setup_data():

    params = {
        "code": "123",
        "_id": "68b70ef826423e500863c1c7"
    }

    body = {
        "description": "new description",
        "brand": "new brand",
        "reference": "new reference",
        "location": ["CX01", "CX02"],
        "image": image_string,
        "measure": "Cartela",
        "quantity_change": 5,
        "stock": 5,
        "keepBuying": False,
        "warehouse": {
            "quantity_change": 10,
            "stock": 10,
            "measure": "Cartela",
            "location": ["CX01", "CX02"]
            }
        }
        
    return params, body


def test_product_validate_schema_update_sucessfully(valid_setup_data):

    params, body = valid_setup_data

    update_product_validator_request(body, params)


def test_only_warehouse_update_successfully(valid_setup_data):

    params, body = valid_setup_data

    body_warehouse = {**body["warehouse"]}

    update_product_validator_request(body_warehouse, params)


def test_product_measure_with_invalid_value_return_error(valid_setup_data):

    params, body = valid_setup_data

    body["measure"] = "Kg"

    with pytest.raises(HttpUnprocessableEntity):
        update_product_validator_request(body, params)
    

def test_warehouse_measure_with_invalid_value_return_error(valid_setup_data):

    params, body = valid_setup_data

    body["warehouse"]["measure"] = "Kg"

    with pytest.raises(HttpUnprocessableEntity):
        update_product_validator_request(body, params)
    

def test_negative_stock_return_error(valid_setup_data):

    params, body = valid_setup_data

    body["stock"] = -10

    with pytest.raises(HttpUnprocessableEntity):
        update_product_validator_request(body, params)
    

def test_negative_warehouse_stock_return_error(valid_setup_data):

    params, body = valid_setup_data

    body["warehouse"]["stock"] = -10

    with pytest.raises(HttpUnprocessableEntity):
        update_product_validator_request(body, params)


def test_validate_wrong_input_type_return_error(valid_setup_data):

    params, body = valid_setup_data

    params["code"] = 123
    body["location"] = "CX15"
    body["keepBuying"] = "False"

    with pytest.raises(HttpUnprocessableEntity):

        update_product_validator_request(body, params)


def test_empty_body_fields_return_error(valid_setup_data):

    params, body = valid_setup_data

    body["description"] = "",
    body["stock"] = 0,
    body["image"] = "",
    body["brand"] = "",
    body["reference"] = "",
    body["location"] = [],
    body["measure"] = "",
    body["keepBuying"] = False, 
    body["quantity_change"] = 0   
    

    with pytest.raises(HttpUnprocessableEntity):

        update_product_validator_request(body, params)


def test_partial_body_successfully(valid_setup_data):

    params, body = valid_setup_data

    del body["description"]
    del body["image"]
    del body["reference"]
    del body["keepBuying"]

    update_product_validator_request(body, params)


def test_product_dependencies_fields_return_error(valid_setup_data):

    params, body = valid_setup_data

    del body["stock"]

    with pytest.raises(HttpUnprocessableEntity):
        update_product_validator_request(body, params)


def test_warehouse_dependencies_fields_return_error(valid_setup_data):

    params, body = valid_setup_data

    del body["warehouse"]["stock"]

    with pytest.raises(HttpUnprocessableEntity):
        update_product_validator_request(body, params)


def test_product_dependencies_fields_return_error(valid_setup_data):

    params, body = valid_setup_data

    del body["stock"]

    with pytest.raises(HttpUnprocessableEntity):
        update_product_validator_request(body, params)
