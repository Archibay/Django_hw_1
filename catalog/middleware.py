import datetime
from catalog.models import Logs
from django.http import JsonResponse


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        print("before response")
        response = self.get_response(request)
        q = Logs(path=request.path, method=request.method, timestamp=datetime.datetime.now(), values=1)
        Logs.save(q)
        # Code to be executed for each request/response after
        # the view is called.

        return response
