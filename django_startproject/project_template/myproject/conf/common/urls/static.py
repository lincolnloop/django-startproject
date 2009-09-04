import sys
from django.conf import settings
from django.conf.urls.defaults import *


urlpatterns = []


# Serve up static media if we're running the local development server.
if 'runserver' in sys.argv or 'testserver' in sys.argv:
    urlpatterns += patterns('django.views.static',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^%s(?P<path>.*)$' % settings.STATIC_URL[1:], 'serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    )
