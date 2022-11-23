import configparser
from typing import Any
from django.apps import AppConfig


class TrackerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tracker"

    def __init__(self, app_name: Any, app_module: Any):
        super().__init__(app_name, app_module)
        self._jira_server_info = None
        self._jira_project = None
        self._jira_issue_type = None


    @property
    def jira_server_info(self):
        return self._jira_server_info

    @property
    def jira_project(self):
        return self._jira_project

    @property
    def jira_issue_type(self):
        return self._jira_issue_type

    def ready(self):
        cfg_parser = configparser.ConfigParser()
        cfg_parser.read('jira.credentials.ini')
        cfg = cfg_parser['nimbus']

        self._jira_project = cfg['project']
        self._jira_issue_type = cfg['issue_type']
        self._jira_server_info = {
            "server": cfg['server'],
            "basic_auth": (
                cfg['user'],
                cfg['token'],
            ),
        }
