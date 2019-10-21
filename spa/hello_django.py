from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.http import HttpResponse
from django.urls import path


settings.configure(
    ROOT_URLCONF=__name__,
)

def hello_world(request):
    return HttpResponse(request.headers.get('foo'))

urlpatterns = [
    path("", hello_world),
]

def wrapped_app(environ, start_response):
    environ['HTTP_FOO'] = 'Bar'
    return app(environ, start_response)

app = WSGIHandler()