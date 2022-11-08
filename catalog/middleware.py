import datetime
from catalog.models import Logs


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        if request.path.find('admin') > 0:
            pass
        else:
            if request.method == 'POST':
                q = request.POST
            else:
                q = request.GET
            # m = request.method
            q = Logs(path=request.path, method=Logs.CMethod[request.method], timestamp=datetime.datetime.now(),
                     values=q)
            Logs.save(q)
        # Code to be executed for each request/response after
        # the view is called.

        return response
