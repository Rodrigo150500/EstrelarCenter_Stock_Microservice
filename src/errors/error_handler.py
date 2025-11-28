from .types.http_unavailable_service_error import HttpUnavailableServiceError

from src.main.http_types.http_response import HttpResponse

def error_handler(error):

    if(isinstance(error, (HttpUnavailableServiceError))):

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
