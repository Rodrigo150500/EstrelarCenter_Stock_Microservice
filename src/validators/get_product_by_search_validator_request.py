from bson.objectid import ObjectId
from bson.errors import InvalidId

from cerberus import Validator

from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntity

def get_product_by_search_validator_request(params: dict) -> None:

    params_validator = Validator({
        "search": {"type": "string", "required": True, "empty": False},
        "fields": {"type": "list", "required": True, "schema": {"type": "string", "allowed": ["description", "reference", "brand"]}},
        "last_id": {"type": "string", "required": False, "nullable": True}        
    })

    try:

        if (params["last_id"]):
            ObjectId(params["last_id"])
  
    except (InvalidId) as exception:

        print(f"Error:[GetProductBySearchValidatorRequest][last_id]: {str(exception)}")
        
        raise HttpUnprocessableEntity(f"Error: {str(exception)}")
    

    response = params_validator(params)

    if response is False:

        error = params_validator.errors
        error_key_message = list(error.keys())[0]
        error_message = error[error_key_message]

        formatted_error_message = f"Erro no campo {error_key_message}\n{error_message}"

        print(f"Error:[GetProductBySearchValidatorRequest][Params]: {formatted_error_message}")

        raise HttpUnprocessableEntity(
        message=params_validator.errors)