from bson.objectid import ObjectId

def get_all_products_sucessfully_data():

    get_all_products = [{
        "_id": ObjectId("64a7f3f5f1c2e3b1a5d6e7f8"),
        "16":[{
            "code": "16",
            "description": "IMA BORBOLETA C/04",
            "brand": "MAX PING",
            "reference": "16",
            "amount": 0,
            "location": "",
            "last_change": "+4  23/09/2025 17:06:12",
            "stock": 4,
            "measure": "Unidade",
            "image": "http://example.com/image1.jpg"
        },{
            "code": "16",
            "description": "IMA BORBOLETA C/04 A1",
            "brand": "Ima brand",
            "reference": "16",
            "amount": 0,
            "location": "",
            "last_change": "+4  23/09/2025 17:06:12",
            "stock": 4,
            "measure": "Unidade",
            "image": "http://example.com/image1.jpg"
        }]
    },{
        "_id": ObjectId("64a7f3f5f1c2e3b1a5d6e7f8"),
        "32":[{
            "code": "32",
            "description": "IMA BORBOLETA C/04",
            "brand": "MAX PING",
            "reference": "16",
            "amount": 0,
            "location": "",
            "last_change": "+4  23/09/2025 17:06:12",
            "stock": 4,
            "measure": "Unidade",
            "image": "http://example.com/image1.jpg"
        },{
            "code": "32",
            "description": "IMA BORBOLETA C/04 A1",
            "brand": "Ima brand",
            "reference": "16",
            "amount": 0,
            "location": "",
            "last_change": "+4  23/09/2025 17:06:12",
            "stock": 4,
            "measure": "Unidade",
            "image": "http://example.com/image1.jpg"
        }]
    }]

    data = {
        "get_all_products": get_all_products
    }

    return data