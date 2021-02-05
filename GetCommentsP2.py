from googleapiclient.discovery import build
from apiclient import errors
import os.path
import pickle

def retrieve_comments(service, file_id):
	"""Retrieve a list of comments.

	Args:
		service: Drive API service instance.
		file_id: ID of the file to retrieve comments for.
	Returns:
		List of comments.
	"""
	try:
		comments = service.comments().list(fileId=file_id).execute()
		return comments.get('items', [])
	except errors.HttpError as error:
		print('An error occurred: %s' % error)
	return None
if os.path.exists('token.pickle'):
	with open('token.pickle', 'rb') as token:
		creds = pickle.load(token)
service = build('drive', 'v3', credentials=creds)
print(retrieve_comments(service, "1SrRYng27CXKI6oZrGSJTpXvu-nK6JNB4wN3jt9A7Fqc"))