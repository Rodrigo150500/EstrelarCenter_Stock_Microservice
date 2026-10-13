import pytest

from unittest.mock import ANY

from datetime import datetime

from src.domain.entity.product_entity import ProductEntity

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

from bson import ObjectId

def valid_setup_data_create():

    data_product = {
        "code": "PRD-84920",
        "description": "Parafusadeira e Furadeira Impacto 18V Brushless",
        "brand": "Makita",
        "reference": "DHP485RTJ",
        "location": [
            "CX01",
            "P03",
            "CX04"
        ],
        "image": "https://images.example.com/products/dhp485rtj.jpg",
        "measure": "Unidade",
        "quantity_change": 5,
        "stock": 42,
        "keepBuying": True,
    }

    data_warehouse = {
        "code": "PRD-84920",
        "description": "Parafusadeira e Furadeira Impacto 18V Brushless",
        "brand": "Makita",
        "reference": "DHP485RTJ",
        "location": [
            "CX01",
            "P03",
            "CX04"
        ],
        "image": "https://images.example.com/products/dhp485rtj.jpg",
        "measure": "Unidade",
        "quantity_change": 5,
        "stock": 42,
        "keepBuying": True,
        "warehouse": {
            "quantity_change": 1,
            "stock": 4,
            "measure": "Caixa"
        }
    }

    return {
        "warehouse": data_warehouse,
        "product": data_product
    }


    code = "ABC123"

    data_product = {
        "_id": ObjectId(),
        "description": "Parafusadeira e Furadeira Impacto 18V Brushless",
        "brand": "Makita",
        "reference": "DHP485RTJ",
        "location": [
            "CX01",
            "P03",
            "CX04"
        ],
        "image": "https://images.example.com/products/dhp485rtj.jpg",
        "measure": "Unidade",
        "quantity_change": 5,
        "last_change": datetime.now(),
        "stock": 42,
        "keepBuying": True,
    }

    data_warehouse = {
        "_id": ObjectId(),
        "description": "Parafusadeira e Furadeira Impacto 18V Brushless",
        "brand": "Makita",
        "reference": "DHP485RTJ",
        "location": [
            "CX01",
            "P03",
            "CX04"
        ],
        "image": "https://images.example.com/products/dhp485rtj.jpg",
        "measure": "Unidade",
        "last_change": datetime.now(),
        "quantity_change": 5,
        "stock": 42,
        "keepBuying": True,
        "warehouse": {
            "quantity_change": 1,
            "stock": 4,
            "measure": "Caixa",
            "location": ["CX01"],
            "last_change": datetime.now()
        }
    }

    return {
        "code": code,
        "product": data_product,
        "warehouse": data_warehouse
    }


    data_product = {
        "_id": ObjectId(),
        "code": "ABC123",
        "variants":[{
            "_id": ObjectId(),
            "description": "Parafusadeira e Furadeira Impacto 18V Brushless",
            "brand": "Makita",
            "reference": "DHP485RTJ",
            "location": [
                "CX01",
                "P03",
                "CX04"
            ],
            "image": "https://images.example.com/products/dhp485rtj.jpg",
            "measure": "Unidade",
            "last_change": datetime.now(),
            "quantity_change": 5,
            "stock": 42,
            "keepBuying": True,
            "warehouse": {
                "quantity_change": 1,
                "stock": 4,
                "measure": "Caixa",
                "location": ["CX01"],
                "last_change": datetime.now()
            }
        },
        {
            "_id": ObjectId(),
            "description": "Parafusadeira e Furadeira Impacto 18V Brushless",
            "brand": "Makita",
            "reference": "DHP485RTJ",
            "location": [
                "CX01",
                "P03",
                "CX04"
            ],
            "image": "https://images.example.com/products/dhp485rtj.jpg",
            "measure": "Unidade",
            "last_change": datetime.now(),
            "quantity_change": 5,
            "stock": 42,
            "keepBuying": True,
            "warehouse": {
                "quantity_change": 1,
                "stock": 4,
                "measure": "Caixa",
                "location": ["CX01"],
                "last_change": datetime.now()
            }
        }
        
        ]
    }

    return {
        "product": data_product
    }

def valid_setup_data_update():

    data_product = {
        "description": "new description",
        "brand": "new brand",
        "reference": "new reference",
        "location": ["P15"],
        "image": "image string",
        "measure": "Pacote",
        "quantity_change": 10,
        "stock": 10,
        "keepBuying": False
    }

    data_warehouse = {
        "description": "new description",
        "brand": "new brand",
        "reference": "new reference",
        "location": ["P15"],
        "image": "image string",
        "measure": "Pacote",
        "quantity_change": 10,
        "stock": 10,
        "keepBuying": False,
        "warehouse": {
            "quantity_change": 5,
            "stock": 5,
            "measure": "Caixa"
        }
    }

    return {
        "warehouse": data_warehouse,
        "product": data_product
    }


#-------------------------CREATE---------------------------
def test_business_rules_create_with_warehouse_successfully():

    data_warehouse = valid_setup_data_create()["warehouse"]
    expect_warehouse = {**data_warehouse, "_id": ANY, "last_change": ANY}

    product_entity = ProductEntity.create(data_warehouse)

    assert product_entity is not None
    assert product_entity == expect_warehouse


def test_business_rules_create_product_successfully():

    data_product = valid_setup_data_create()["product"]

    product_entity = ProductEntity.create(data_product)

    assert product_entity is not None


def test_measure_allowed_in_product_expect_error():

    data_product = valid_setup_data_create()["product"]

    data_product["measure"] = "Kg"

    with pytest.raises(HttpUnprocessableEntity) as exec_info:

        ProductEntity.create(data_product)

    error = exec_info.value.message

    assert error == "O campo Medida deve ser apenas: Unidade, Caixa, Pacote, Fardo, Saco, Rolo, Cartela, Bloco ou Pote"


def test_measure_allowed_in_warehouse_expect_error():

    data_warehouse = valid_setup_data_create()["warehouse"]

    data_warehouse["warehouse"]["measure"] = "Kg"

    with pytest.raises(HttpUnprocessableEntity) as exec_info:

        ProductEntity.create(data_warehouse)

    error = exec_info.value.message

    assert error == "O campo Medida do Galpão deve ser apenas: Unidade, Caixa, Pacote, Fardo, Saco, Rolo, Cartela, Bloco ou Pote"


def test_missing_required_fields_for_product_expect_error():

    data_product = valid_setup_data_create()["product"]

    del data_product["code"]

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        ProductEntity.create(data_product)

    error = exec_info.value.message

    assert error == "Campo obrigatório: [code] não encontrado"


def test_missing_required_fields_for_warehouse_expect_error():
    
    data_wahouse = valid_setup_data_create()["warehouse"]

    del data_wahouse["warehouse"]["stock"]

    with pytest.raises(HttpUnprocessableEntity) as exec_info:

        ProductEntity.create(data_wahouse)

    error = exec_info.value.message

    assert error == "Campo obrigatório: [stock] não encontrado" 


def test_empty_fields_product_in_required_fields_expect_error():

    data_product = valid_setup_data_create()["product"]

    data_product["code"] = ""

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        ProductEntity.create(data_product)

    error = exec_info.value.message

    assert error == "O campo code não pode estar vazio"
    

def test_empty_fields_warehouse_in_required_fields_expect_error():

    data_warehouse= valid_setup_data_create()["warehouse"]

    data_warehouse["stock"] = ""

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        ProductEntity.create(data_warehouse)

    error = exec_info.value.message

    assert error == "O campo stock não pode estar vazio"
    

def test_negative_stock_in_product_expect_error():

    data_product = valid_setup_data_create()["product"]

    data_product["stock"] = -1

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        ProductEntity.create(data_product)

    error = exec_info.value.message

    assert error == "O campo Estoque não pode ser negativo"
    

def test_negative_stock_in_warehouse_expect_error():

    data_warehouse = valid_setup_data_create()["warehouse"]

    data_warehouse["warehouse"]["stock"] = -1

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        ProductEntity.create(data_warehouse)

    error = exec_info.value.message
    
    assert error == "O campo Estoque do Galpão não pode ser negativo"


#-------------------------UPDATE---------------------------

def test_bussiness_rules_update_with_warehouse_successfully():

    data_warehouse = valid_setup_data_update()["warehouse"]
    expect_warehouse = {**data_warehouse, "last_change": ANY}

    product_entity = ProductEntity().update(data_warehouse)

    assert product_entity is not None
    assert "last_change" in product_entity
    assert product_entity == expect_warehouse

def test_bussiness_rules_update_product_successfully():

    data_product = valid_setup_data_update()["product"]
    expect_product = {**data_product, "last_change": ANY}

    product_entity = ProductEntity().update(data_product)

    assert product_entity is not None
    assert "last_change" in product_entity

    assert product_entity == expect_product


def test_empty_values_for_required_field_product_expect_error():

    data_product = valid_setup_data_update()["product"]

    data_product["description"] = ""

    with pytest.raises(HttpUnprocessableEntity) as exec_info:

        ProductEntity().update(data_product)

    error = exec_info.value

    assert error.message == "O campo description não pode estar vazio"


def test_empty_values_for_required_field_warehouse_expect_error():

    data_product = valid_setup_data_update()["warehouse"]

    data_product["warehouse"]["measure"] = ""

    with pytest.raises(HttpUnprocessableEntity) as exec_info:

        ProductEntity().update(data_product)

    error = exec_info.value

    assert error.message == "O campo measure não pode estar vazio"


def test_measure_allowed_in_update_product_expect_error():
    pass

def test_measure_allowed_in_update_warehouse_expect_error():
    pass

def test_negative_stock_in_update_product_expect_error():
    pass

def test_measure_allowed_in_update_warehouse_expect_error():
    pass