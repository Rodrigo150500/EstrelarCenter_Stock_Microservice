from abc import ABC, abstractmethod

from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class InserProductMongoUseCaseInterface(ABC):

    @abstractmethod
    def handle(http_request: HttpRequest) -> HttpResponse:
        pass