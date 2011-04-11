from django.conf.urls.defaults import patterns, include
from django.conf.urls.static import static
from django.conf import settings

CONF_MODULE = '%s.conf' % settings.PROJECT_MODULE_NAME

urlpatterns = patterns('',
    (r'', include('%s.urls' % CONF_MODULE)),
    (r'', include('%s.common.urls.admin' % CONF_MODULE)),
)
if settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
