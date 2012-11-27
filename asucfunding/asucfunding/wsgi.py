# wsgi_xlab.py
import site
import os
import sys

SITE_DIR = '/opt/django-trunk/'

site.addsitedir(SITE_DIR) 

sys.path.append(SITE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'xlab_server.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

import django.core.handlers.wsgi
class ForcePostHandler(django.core.handlers.wsgi.WSGIHandler):
    """Workaround for: http://lists.unbit.it/pipermail/uwsgi/2011-February/001395.html
    """
    def get_response(self, request):
        request.POST # force reading of POST data
        return super(ForcePostHandler, self).get_response(request)

application = ForcePostHandler()