import logging
from contextlib import closing
from functools import wraps
from types import SimpleNamespace

from jira import JIRA

logger = logging.getLogger("django")


def _log_suppress_return(log_msg="", return_on_failure=None):
    # Using factory pattern to parameterize the decorator
    def __log_suppress_return(func):
        @wraps(func)
        def _wrapped(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                # log exception and suppress by just forgetting it
                logger.exception(log_msg)

            # return the failure value specified by the function
            return return_on_failure

        return _wrapped

    return __log_suppress_return


def with_jira(jira_func):
    """
    jira_func is any function with a JIRA instance in it's first argument.
    It returns a wrapped version where the JIRA object has been swapped out
    for an dictionary containing the necessary server information to construct
    a JIRA object.
    """

    @wraps(jira_func)
    def _wrapped(jira_server_info, *args, **kwargs):
        with closing(JIRA(**jira_server_info)) as jira:
            return jira_func(jira, *args, **kwargs)

    return _wrapped


@with_jira
@_log_suppress_return(
    log_msg="Jira Issue ticket creation failed.",
    return_on_failure=None
)
def create_ticket(jira_connection, ticket, project, issue_type):
    issue_dict = {
        'project': {'key': project},
        'summary': _get_ticket_summary(ticket),
        'description': _get_ticket_synopsis(ticket),
        'customfield_10011': _get_ticket_summary(ticket),
        'issuetype': {'name': issue_type}
    }

    issue = jira_connection.create_issue(fields=issue_dict)
    return issue.key


@with_jira
@_log_suppress_return(
    log_msg="Jira Issue ticket edit failed.",
    return_on_failure=False
)
def edit_ticket(jira_connection, jira_id, ticket):
    jira_connection.add_comment(jira_id, "Ticket was edited:\n" + _get_ticket_synopsis(ticket))
    return True


@with_jira
@_log_suppress_return(
    log_msg="Jira Issue ticket status update failed.",
    return_on_failure=False
)
def update_ticket_status(jira_connection, jira_id, ticket):
    jira_connection.add_comment(jira_id, "Ticket status was updated to: " + ticket.get_ticket_status[1])
    return True


@with_jira
@_log_suppress_return(
    log_msg="Jira Issue ticket deletion failed.",
    return_on_failure=False
)
def delete_ticket(jira_connection, jira_id, ticket):
    jira_connection.add_comment(jira_id, "Ticket was deleted")
    return True


def _get_ticket_summary(ticket):
    summary = "Data Upload for Study " + ticket.study_name
    return summary


def _get_ticket_synopsis(ticket):
    synopsis = "Name: " + ticket.name + "\n" + \
               "Email: " + ticket.email + "\n" + \
               "Organization: " + ticket.organization + "\n" + \
               "Study Name: " + ticket.study_name + "\n" + \
               "Study ID: " + ticket.study_id + "\n" + \
               "dbGaP Consent Group Code: " + ticket.consent_code + "\n" + \
               "Data Size: " + ticket.data_size + "\n" + \
               "Dataset Description: " + ticket.dataset_description + "\n" + \
               "Google Email: " + ticket.google_email + "\n" + \
               "AWS IAM: " + ticket.aws_iam + "\n" + \
               "Is Test Data: " + str(ticket.is_test_data) + "\n" + \
               "Ticket Review Comment: " + ticket.ticket_review_comment

    return synopsis


def main():
    import configparser

    config = configparser.ConfigParser()
    config.read('jira.credentials.ini')

    user = config['nimbus']['user']
    server = config['nimbus']['server']
    token = config['nimbus']['token']

    jira_info = {"server": server, "basic_auth": (user,token),}
    ticket = SimpleNamespace(name='Ann Van', email='ann@nimbusinformatics.com', organization='Nimbus Informatics',
                             study_name='Test Study', study_id='phs0009999', consent_code='c1', data_size='1 MB',
                             dataset_description='test description', google_email='ann@nimbusinformatics.com',
                             aws_iam='XXX', is_test_data='No', ticket_review_comment='Approved')
    print("running tests on jira_ticket.py")
    jira_id = create_ticket(jira_info, ticket, config['nimbus']['project'], config['nimbus']['issue_type'])
    print("created ticket with id " + jira_id)
    result = edit_ticket(jira_info, jira_id, ticket)
    result = delete_ticket(jira_info, jira_id, ticket)
    return


if __name__ == "__main__":
    main()
