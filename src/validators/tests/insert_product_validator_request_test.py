import pytest

from src.validators.insert_product_validator_request import insert_product_validator_request

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

def valid_setup_request():

    body_request = {
            "code": "10",
            "description": "Chocolate Suflair 1kg",
            "brand": "Nestle",
            "reference": "SF-001",
            "location": ["CX01", "CX02"],
            "image": "image string",
            "measure": "Caixa",
            "quantity_change": 5,
            "stock": 10,
            "keepBuying": False,
            "warehouse":{
                "quantity_change": 5,
                "stock": 3,
                "measure": "Caixa",
                "location": ["CX33", "P01"]
            }
        }

    return body_request

def test_validator_schema_return_successfully():

    body_request = valid_setup_request()

    insert_product_validator_request(body_request)


def test_validator_schema_without_warehouse_insert_return_sucessfully():

    body_request = valid_setup_request()

    del body_request["warehouse"]

    insert_product_validator_request(body_request)


def test_empty_fields_for_warehouse_return_error():

    body_request = valid_setup_request()

    body_request["warehouse"]["quantity_change"] = ""
    body_request["warehouse"]["stock"] = ""
    body_request["warehouse"]["measure"] = ""
    body_request["warehouse"]["location"] = ""

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        insert_product_validator_request(body_request)

    error = exec_info.value

    expect_total_errors = len(error.message["warehouse"][0].keys())

    assert "quantity_change" in error.message["warehouse"][0]
    assert "stock" in error.message["warehouse"][0]
    assert "measure" in error.message["warehouse"][0]
    assert "location" in error.message["warehouse"][0]
    
    assert expect_total_errors == 4


def test_empty_fields_without_warehouse_return_error():

    body_request = valid_setup_request()

    del body_request["warehouse"]

    for key, _ in body_request.items():
        body_request[key] = ""

    with pytest.raises(HttpUnprocessableEntity) as exec_info:

        insert_product_validator_request(body_request) 
    
    error = exec_info.value

    expect_total_errors = len(error.message.keys())

    assert "code" in error.message
    assert "description" in error.message
    assert "brand" not in error.message
    assert "reference" not in error.message
    assert "location" in error.message
    assert "image" not in error.message
    assert "stock" in error.message
    assert "keepBuying" in error.message
    
    assert expect_total_errors == 7

def test_just_the_required_fields_return_successfully():

    body_request = valid_setup_request()

    del body_request["brand"]
    del body_request["reference"]
    del body_request["location"]
    del body_request["warehouse"]

    insert_product_validator_request(body_request)


def test_fill_the_fields_with_wrong_type_return_error():

    body_request = valid_setup_request()

    body_request["code"] = 10 #Should be string
    body_request["stock"] = "15" #Should be integer
    body_request["keepBuying"] = "False" #Should be boolean
    body_request["warehouse"]["location"] = False #Should be a list
    body_request["warehouse"]["stock"] = "44" #"Should be integer"

    with pytest.raises(HttpUnprocessableEntity) as exec_info:

        insert_product_validator_request(body_request)      

    error = exec_info.value

    errors_warehouse = len(error.message["warehouse"][0].keys())

    expect_total_errors = len(error.message.keys()) - 1 + errors_warehouse

    assert "code" in error.message
    assert "stock" in error.message
    assert "keepBuying" in error.message
    assert "location" in error.message["warehouse"][0]
    assert "stock" in error.message["warehouse"][0]
    
    assert expect_total_errors == 5


def test_missing_required_fields_return_error():

    body_request = valid_setup_request()

    del body_request["code"]
    del body_request["description"]
    del body_request["image"]
    del body_request["measure"]
    del body_request["quantity_change"]
    del body_request["stock"]
    del body_request["keepBuying"]
    del body_request["warehouse"]["quantity_change"]
    del body_request["warehouse"]["stock"]
    del body_request["warehouse"]["measure"]

    with pytest.raises(HttpUnprocessableEntity) as exec_info:

        insert_product_validator_request(body_request)

    error = exec_info.value

    errors_warehouse = len(error.message["warehouse"][0].keys())

    expect_total_errors = len(error.message.keys()) -1 + errors_warehouse

    assert "code" in error.message
    assert "description" in error.message
    assert "image" in error.message
    assert "measure" in error.message
    assert "quantity_change" in error.message
    assert "stock" in error.message
    assert "keepBuying" in error.message
    assert "quantity_change" in error.message["warehouse"][0]
    assert "stock" in error.message["warehouse"][0]
    assert "measure" in error.message["warehouse"][0]

    assert expect_total_errors == 10


def test_required_field_from_warehouse():

    body_request = valid_setup_request()

    del body_request["warehouse"]["quantity_change"]
    del body_request["warehouse"]["stock"]
    del body_request["warehouse"]["measure"]


    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        insert_product_validator_request(body_request)

    error = exec_info.value
    expect_total_errors = len(error.message["warehouse"][0].keys())

    assert "quantity_change" in error.message["warehouse"][0]    
    assert "stock" in error.message["warehouse"][0]    
    assert "measure" in error.message["warehouse"][0]  
    assert expect_total_errors == 3


def test_measure_with_invalid_value_return_error():

    body_request = valid_setup_request()
    body_request["measure"] = "Kilograma"

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        insert_product_validator_request(body_request)

    error = exec_info.value

    expect_total_errors = len(error.message.keys())

    assert "measure" in error.message

    assert expect_total_errors == 1


def test_warehouse_measure_with_invalid_value_return_error():

    body_request = valid_setup_request()
    body_request["warehouse"]["measure"] = "Kilograma"

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        insert_product_validator_request(body_request)

    error = exec_info.value

    expect_total_errors = len(error.message["warehouse"][0].keys())

    assert "measure" in error.message["warehouse"][0]
    
    assert expect_total_errors == 1


def test_stock_less_than_zero_return_error():

    body_request = valid_setup_request()
    body_request["stock"] = -1

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        insert_product_validator_request(body_request)

    error = exec_info.value

    expect_total_errors = len(error.message.keys())

    assert "stock" in error.message

    assert expect_total_errors == 1