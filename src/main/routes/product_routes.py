from flask import Blueprint, jsonify, request

from src.main.http_types.http_request import HttpRequest

from src.main.composer.mongo.get_product_composer import get_product_composer
from src.main.composer.mongo.insert_product_composer import insert_product_composer
from src.main.composer.mongo.delete_product_composer import delete_product_composer
from src.main.composer.mongo.update_product_composer import update_product_composer
from src.main.composer.mongo.get_product_by_search_composer import get_product_by_search_composer
from src.main.composer.mongo.remove_item_composer import remove_item_composer
from src.main.composer.mongo.insert_new_variant_composer import insert_new_variant_composer

from src.errors.error_handler import error_handler

product_routes_bp = Blueprint("product_bp", __name__)

@product_routes_bp.route("/product/<code>", methods=["GET"])
def get_product_by_code(code: str):

    try:

        http_request = HttpRequest(params={"code": code})

        use_case = get_product_composer()

        response = use_case.handle(http_request)

        return jsonify(response.body), response.status_code

    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code


@product_routes_bp.route("/product", methods=["POST"])
def insert_product():

    try:

        http_request = HttpRequest(body=request.json)

        use_case = insert_product_composer()

        response = use_case.handle(http_request)

        return jsonify(response.body), response.status_code

    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code


@product_routes_bp.route("/product/<code>", methods=["DELETE"])
def delete_product_by_code(code: str):

    try:

        http_request = HttpRequest(params={"code": code})

        use_case = delete_product_composer()

        response = use_case.handle(http_request)

        return jsonify(response.body), response.status_code

    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code
        

@product_routes_bp.route("/product/<code>/variant/<variant_id>", methods=["PATCH"])
def update_product_variant(code: str, variant_id: str):

    try:

        http_request = HttpRequest(params={"code": code, "_id": variant_id}, body=request.json)

        use_case = update_product_composer()

        response = use_case.handle(http_request)

        return jsonify(response.body), response.status_code
    
    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code


@product_routes_bp.route("/product/search", methods=["GET"])
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
def remove_item_variant(code: str, variant_id: str):

    try:

        http_request = HttpRequest(params={"code": code, "_id": variant_id})

        use_case = remove_item_composer()

        response = use_case.handle(http_request)

        return jsonify(response.body), response.status_code
    
    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code
    
    
@product_routes_bp.route("/product/<code>/variant", methods=["POST"])
def insert_product_variant(code: str):
    
    try:
        params = {"code": code}
        body = request.json

        http_request = HttpRequest(body=body, params=params)

        use_case = insert_new_variant_composer()

        response = use_case.handle(http_request)

        return jsonify(response.body), response.status_code
    
    except Exception as exception:

        response = error_handler(exception)

        return jsonify(response.body), response.status_code
