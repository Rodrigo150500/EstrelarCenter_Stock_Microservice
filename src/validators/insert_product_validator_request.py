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
                "localtion": {"type": "list", "required": False}
              }
            }
            })

  response = body_validate.validate(body)


  if response is False:
    error = body_validate.errors
    error_key_message = list(error.keys())[0]
    error_message = error[error_key_message]
    print()
    print([error][0])


    formatted_error_message = f"Erro no campo {error_key_message}\n{error_message}"

    print(f"Error:[InsertProductValidatorRequest][Body]: {formatted_error_message}")

    raise HttpUnprocessableEntity(
      message=formatted_error_message
    )

