from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from cerberus import Validator


def insert_product_validator_request(body: dict):

  body_validate = Validator({         
            'code':{'type': 'string', 'required': True, "empty": False},
            'variants': {
              "type": "list",
              "required": True,
              "schema": {
                "type": "dict",
                "schema":{
                    "description": {"type": "string", "required": True},
                    "stock": {"type": "integer", "required": True},
                    "image": {"type": "string", "required": True},
                    "brand": {"type": "string", "required": False},
                    "reference": {"type": "string", "required": False},
                    "last_change": {"type": "datetime", "required": True},
                    "location": {"type": "string", "required": False},
                    "measure": {"type": "string", "required": True},
                    "keepBuying": {"type": "boolean", "required": True}
                }
              }
            }})

  response = body_validate.validate(body)


  if response is False:
    error = body_validate.errors
    error_key_message = list(error.keys())[0]
    error_message = error[error_key_message]

    formatted_error_message = f"Erro no campo {error_key_message}\n{error_message}"

    raise HttpUnprocessableEntity(
      message=formatted_error_message
    )

