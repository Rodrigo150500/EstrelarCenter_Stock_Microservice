def insert_product_sucessfully_data():

    body = {
        'code': "55",
        'description': "Product A",
        'measure': "Unidade",
        'stock': 20,
        'brand': "Kit-Kat",
        'last_change': "2024-06-01T12:00:00Z",
        'image': "http://example.com/image.jpg",
        'location': "CX01",
        'reference': "KIT102",
        'item': 0       
    }

    expected_response = {
        "data": {
            "operation": "update",
            "count": 1,
            "attributes": {                       
                "Descrição": "Product A",
                "Marca": "Kit-Kat",
                "Quantidade": 20,
                "Referência": "KIT102"
            }
        }
    }

    formatted_body = {
        "Descrição": "Product A",
        "Marca": "Kit-Kat",
        "Quantidade": 20,
        "Referência": "KIT102"
    }

    data = {
        "body": body,
        "expected_response": expected_response,
        "formatted_body": formatted_body    
    }

    return data

def insert_product_invalid_body_data():

    body = {
        # 'code': "55",
        'measure': "Unidade",
        'stock': 20,
        'brand': "Kit-Kat",
        'last_change': "2024-06-01T12:00:00Z",
        'image': "http://example.com/image.jpg",
        'location': "CX01",
        'reference': "KIT102",
        'item': 0       
    }

    data = {
        "body": body  
    }

    return data

