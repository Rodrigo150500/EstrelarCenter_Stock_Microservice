from dotenv import load_dotenv
load_dotenv("dev.env")

from src.main.server.server import create_app

def test_insert_product():
    app = create_app()

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

    response = app.test_client().post("/product", json=data_product)

    assert response.status_code == 422