"""
WSGI config for bdcat_data_submission project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import logging

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bdcat_data_submission.settings")
logger = logging.getLogger("django")
logger.info("Starting BDC Data Submission Tracker Application")
application = get_wsgi_application()

