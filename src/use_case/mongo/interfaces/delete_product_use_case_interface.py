from abc import ABC, abstractmethod

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class DeleteProductUseCaseInterface(ABC):
    
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass