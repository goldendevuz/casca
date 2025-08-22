from typing import Callable

from django.http import HttpRequest, HttpResponse


class SimpleAuthMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        # placeholder middleware
        return self.get_response(request)
