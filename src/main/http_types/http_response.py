class HttpResponse:

    def __init__(self, body: str, status_code: int):
        
        self.body = body
        self.status_code = status_code