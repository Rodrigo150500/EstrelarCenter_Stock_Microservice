from .types.http_unavailable_service import HttpUnavailableService
from .types.http_unprocessable_entity import HttpUnprocessableEntity
from .types.http_not_found import HttpNotFound
from .types.http_internal_server_error import HttpInternalServerError


from src.main.http_types.http_response import HttpResponse

def error_handler(error):

    if(isinstance(error, (HttpUnavailableService, HttpUnprocessableEntity, HttpNotFound, HttpInternalServerError))):

        return HttpResponse(
            body={
                'errors':[{
                    "title": error.name,
                    "message": error.message 
                }]
            },
            status_code= error.status_code
        )
    
    else:

        return HttpResponse(
            body={
                "error": {
                    "title": "Server Error",
                    "message": "Server out of working"
                }
            }, status_code=500
        )
