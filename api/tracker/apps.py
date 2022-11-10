import configparser
from typing import Any
from django.apps import AppConfig


class TrackerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tracker"

    def __init__(self, app_name: Any, app_module: Any):
        super().__init__(app_name, app_module)
        self._jira_server_info = None


    @property
    def jira_server_info(self):
        return self._jira_server_info

    def ready(self):
        config = configparser.ConfigParser()
        config.read('jira.credentials.ini')

        user = config['nimbus']['user']
        server = config['nimbus']['server']
        token = config['nimbus']['token']

        self._jira_server_info = {
            "server": server,
            "basic_auth": (user, token),
        }
