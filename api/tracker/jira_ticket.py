from jira import JIRA
from types import SimpleNamespace
import configparser


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
	
def edit_ticket(jira_connection, jira_id, ticket):
	comment = jira_connection.add_comment(jira_id, "Ticket was edited:\n" + _get_ticket_synopsis(ticket))
	return True
	
def update_ticket_status(jira_connection, jira_id, ticket):
	comment = jira_connection.add_comment(jira_id, "Ticket status was updated to: " + ticket.get_ticket_status[1])
	return True
	
def delete_ticket(jira_connection, jira_id, ticket):
	comment = jira_connection.add_comment(jira_id, "Ticket was deleted")
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
	config = configparser.ConfigParser()
	config.read('jira.credentials.ini')

	user = config['nimbus']['user']
	server = config['nimbus']['server']
	token = config['nimbus']['token']

	options = {"server": server}
	jira_connection = JIRA(options, basic_auth=(user, token))
	ticket = SimpleNamespace(name='Ann Van', email='ann@nimbusinformatics.com', organization='Nimbus Informatics', study_name='Test Study', study_id='phs0009999', consent_code='c1', data_size='1 MB', dataset_description='test description', google_email='ann@nimbusinformatics.com',aws_iam='XXX', is_test_data='No', ticket_review_comment='Approved')
	print("running tests on jira_ticket.py") 
	jira_id = create_ticket(jira_connection, ticket, 'MCMP', 'Epic')
	print("created ticket with id " + jira_id) 
	result = edit_ticket(jira_connection, jira_id, ticket)
	result = delete_ticket(jira_connection, jira_id, ticket)
	return
		
if __name__ == "__main__":
    main()
