from .types.http_unavailable_service import HttpUnavailableService
from .types.http_unprocessable_entity import HttpUnprocessableEntity

from src.main.http_types.http_response import HttpResponse

def error_handler(error):

    if(isinstance(error, (HttpUnavailableService, HttpUnprocessableEntity))):

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
