from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from cerberus import Validator


def insert_product_validator_request(body: dict):

  body_validate = Validator({         
            "code":{'type': 'string', 'required': True, "empty": False},
            "description": {"type": "string", "required": True, "empty": False},
            "brand": {"type": "string", "required": False},
            "reference": {"type": "string", "required": False},
            "location": {"type": "list", "required": False},
            "image": {"type": "string", "required": True},
            "measure": {"type": "string", "required": True, "allowed": ["Unidade", "Caixa", "Pacote", "Fardo", "Saco", "Rolo", "Cartela", "Bloco", "Pote"]},
            "quantity_change":{"type": "integer", "required": True},
            "stock": {"type": "integer", "required": True, "min": 0, "empty": False},
            "keepBuying": {"type": "boolean", "required": True},
            "warehouse": {
              "type": "dict",
              "required": False,
              "schema":{
                "quantity_change": {"type": "integer", "required": True, 'empty': False},
                "stock": {"type": "integer", "required": True, "min": 0},
                "measure": {"type": "string", "required": True, "allowed": ["Unidade", "Caixa", "Pacote", "Fardo", "Saco", "Rolo", "Cartela", "Bloco", "Pote"]},
                "location": {"type": "list", "required": False}
              }
            }
            })

  response = body_validate.validate(body)


  if response is False:
    
    error = body_validate.errors

    raise HttpUnprocessableEntity(
      message=error
    )

