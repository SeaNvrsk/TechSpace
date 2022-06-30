import mimetypes

from storages.backends.ftp import FTPStorage
from django.http import HttpResponse


class FTPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        FS = FTPStorage()

        response = self.get_response(request)
        path = request.get_full_path()
        if FS.exists(path):
            file = FS._read(path)
            type, encoding = mimetypes.guess_type(path)
            response = HttpResponse(file, content_type=type)
            response['Content-Disposition'] = u'attachment; filename="{filename}"'.format(filename=path)

        return response
