from myproject.conf.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('You', 'your@email'),
)
MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
# Place the SQLite database into ``[project]/conf/local/`` so it's outside of
# the repository.
DATABASE_NAME = os.path.join(PROJECT_ROOT, PROJECT_MODULE_NAME,
                             'conf', 'local', 'dev.db')

ROOT_URLCONF = '%s.conf.local.urls' % PROJECT_MODULE_NAME

INSTALLED_APPS += (
    'django.contrib.admin',
    'django.contrib.admindocs',
)
