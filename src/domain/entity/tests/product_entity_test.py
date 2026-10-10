import pytest

from src.domain.entity.product_entity import ProductEntity

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

def valid_setup_data():

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

def test_business_rules_create_with_warehouse_successfully():

    data_warehouse = valid_setup_data()["warehouse"]

    product_entity = ProductEntity.create(data_warehouse)

    assert product_entity is not None


def test_business_rules_create_product_entity_successfully():

    data_product = valid_setup_data()["product"]

    product_entity = ProductEntity.create(data_product)

    assert product_entity is not None


def test_measure_allowed_in_product_expect_error():

    data_product = valid_setup_data()["product"]

    data_product["measure"] = "Kg"

    with pytest.raises(HttpUnprocessableEntity) as exec_info:

        ProductEntity.create(data_product)

    error = exec_info.value.message

    assert error == "O campo Medida deve ser apenas: Unidade, Caixa, Pacote, Fardo, Saco, Rolo, Cartela, Bloco ou Pote"


def test_measure_allowed_in_warehouse_expect_error():

    data_warehouse = valid_setup_data()["warehouse"]

    data_warehouse["warehouse"]["measure"] = "Kg"

    with pytest.raises(HttpUnprocessableEntity) as exec_info:

        ProductEntity.create(data_warehouse)

    error = exec_info.value.message

    assert error == "O campo Medida do Galpão deve ser apenas: Unidade, Caixa, Pacote, Fardo, Saco, Rolo, Cartela, Bloco ou Pote"


def test_missing_required_fields_for_product_expect_error():

    data_product = valid_setup_data()["product"]

    del data_product["code"]

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        ProductEntity.create(data_product)

    error = exec_info.value.message

    assert error == "Campo obrigatório: [code] não encontrado"


def test_missing_required_fields_for_warehouse_expect_error():
    
    data_wahouse = valid_setup_data()["warehouse"]

    del data_wahouse["warehouse"]["stock"]

    with pytest.raises(HttpUnprocessableEntity) as exec_info:

        ProductEntity.create(data_wahouse)

    error = exec_info.value.message

    assert error == "Campo obrigatório: [stock] não encontrado" 


def test_empty_fields_product_in_required_fields_expect_error():

    data_product = valid_setup_data()["product"]

    data_product["code"] = ""

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        ProductEntity.create(data_product)

    error = exec_info.value.message

    assert error == "O campo code não pode estar vazio"
    

def test_empty_fields_warehouse_in_required_fields_expect_error():

    data_warehouse= valid_setup_data()["warehouse"]

    data_warehouse["stock"] = ""

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        ProductEntity.create(data_warehouse)

    error = exec_info.value.message

    assert error == "O campo stock não pode estar vazio"
    

def test_negative_stock_in_product_expect_error():

    data_product = valid_setup_data()["product"]

    data_product["stock"] = -1

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        ProductEntity.create(data_product)

    error = exec_info.value.message

    assert error == "O campo Estoque não pode ser negativo"
    

def test_negative_stock_in_warehouse_expect_error():

    data_warehouse = valid_setup_data()["warehouse"]

    data_warehouse["warehouse"]["stock"] = -1

    with pytest.raises(HttpUnprocessableEntity) as exec_info:
        ProductEntity.create(data_warehouse)

    error = exec_info.value.message
    
    assert error == "O campo Estoque não pode ser negativo"

