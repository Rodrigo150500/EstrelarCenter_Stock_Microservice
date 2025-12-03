from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity
from cerberus import Validator


def insert_product_validator_request(body: dict):

  body_validate = Validator({         
            'code':{'type': 'string', 'required': True},
            'description': {'type': 'string', 'required': True},
            'measure': {'type': 'string', 'required': True},
            'stock': {'type': 'integer', 'required': True},
            'brand': {'type': 'string', 'required': False},
            'last_change': {'type': 'string', 'required': False},
            'image': {'type': 'string', 'required': False},
            'location': {'type': 'string', 'required': False},
            'reference': {'type': 'string', 'required': False},
  })

  response = body_validate.validate(body)


  if response is False:
    error = body_validate.errors
    error_key_message = list(error.keys())[0]
    error_message = error[error_key_message]

    formatted_error_message = f"Erro no campo {error_key_message}\n{error_message}"

    raise HttpUnprocessableEntity(
      message=formatted_error_message
    )

