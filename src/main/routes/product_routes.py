from flask import Blueprint, jsonify, request

from flasgger import swag_from

from src.main.http_types.http_request import HttpRequest

from src.main.composer.mongo.get_product_composer import get_product_composer
from src.main.composer.mongo.insert_product_composer import insert_product_composer
from src.main.composer.mongo.delete_product_composer import delete_product_composer
from src.main.composer.mongo.update_product_composer import update_product_composer
from src.main.composer.mongo.get_product_by_search_composer import get_product_by_search_composer
from src.main.composer.mongo.delete_variant_composer import delete_variant_composer
from src.main.composer.mongo.insert_new_variant_composer import insert_new_variant_composer

from src.validators.insert_product_validator_request import insert_product_validator_request
from src.validators.get_product_validator_request import get_product_validator_request
from src.validators.insert_product_validator_request import insert_product_validator_request
from src.validators.delete_product_validator_request import delete_product_validator_request
from src.validators.update_product_validator_request import update_product_validator_request
from src.validators.delete_variant_validator_request import delete_variant_validator_request
from src.validators.insert_new_variant_request import insert_new_variant_request

from src.errors.error_handler import error_handler

product_routes_bp = Blueprint("product_bp", __name__)

@product_routes_bp.route("/product/<code>", methods=["GET"])
@swag_from("../../docs/get_product_by_code_doc.yml")
def get_product_by_code(code: str):

    try:        

        params = {"code": code}

        get_product_validator_request(params)

        http_request = HttpRequest(params=params, header=request.host)

        use_case = get_product_composer()

        response = use_case.handle(http_request)

        return jsonify(response.body), response.status_code

    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code


@product_routes_bp.route("/product", methods=["POST"])
@swag_from("../../docs/insert_product_doc.yml")
def insert_product():

    try:

        body = request.json

        insert_product_validator_request(body)
            
        http_request = HttpRequest(body=body, header=request.host)

        use_case = insert_product_composer()

        response = use_case.handle(http_request)

        return jsonify(response.body),response.status_code

    except Exception as exception:
        print(exception)
        response = error_handler(exception)

        return jsonify(response.body), response.status_code


@product_routes_bp.route("/product/<code>", methods=["DELETE"])
@swag_from("../../docs/delete_product_by_code_doc.yml")
def delete_product_by_code(code: str):

    try:

        params = {"code": code}

        delete_product_validator_request(params)

        http_request = HttpRequest(params={"code": code})

        use_case = delete_product_composer()

        response = use_case.handle(http_request)

        return jsonify(response.body), response.status_code

    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code
        

@product_routes_bp.route("/product/<code>/variant/<variant_id>", methods=["PATCH"])
@swag_from("../../docs/update_product_doc.yml")
def update_product_variant(code: str, variant_id: str):

    try:

        params = {"code": code, "_id": variant_id}
        body = request.json

        update_product_validator_request(body, params)

        http_request = HttpRequest(params={"code": code, "_id": variant_id}, body=request.json, header=request.host)
        
        use_case = update_product_composer()

        response = use_case.handle(http_request)

        return jsonify(response.body), response.status_code
    
    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code


@product_routes_bp.route("/product/search", methods=["GET"])
@swag_from("../../docs/get_product_by_search_doc.yml")
def get_product_by_search():
    
    try:
        search = request.args.get("search") 

        last_id = request.args.get("last_id")
        
        fields_raw = request.args.get("fields")
        fields = fields_raw.split(",") if fields_raw else []

        params = {
            "search": search,
            "fields": fields,
            "last_id": last_id
        }

        http_request = HttpRequest(params=params)
        use_case = get_product_by_search_composer()

        response = use_case.handle(http_request)

        return jsonify(response.body), response.status_code

    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code
    

@product_routes_bp.route("/product/<code>/variant/<variant_id>", methods=["DELETE"])
@swag_from("../../docs/remove_item_doc.yml")
def delete_variant(code: str, variant_id: str):

    try:

        params = {"code": code, "_id": variant_id}

        delete_variant_validator_request(params)

        http_request = HttpRequest(params={"code": code, "_id": variant_id})

        use_case = delete_variant_composer()

        response = use_case.handle(http_request)

        return jsonify(response.body), response.status_code
    
    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code
    
    
@product_routes_bp.route("/product/<code>/variant", methods=["POST"])
@swag_from("../../docs/insert_new_variant_by_code_doc.yml")
def insert_product_variant(code: str):
    
    try:
        params = {"code": code}
        body = request.json

        insert_new_variant_request(params, body)

        http_request = HttpRequest(body=body, params=params, header=request.host)

        use_case = insert_new_variant_composer()

        response = use_case.handle(http_request)

        return jsonify(response.body), response.status_code
    
    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code
