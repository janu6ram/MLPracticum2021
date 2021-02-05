from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors

def read_json(link, s):
    import json
    data = json.loads(json.dumps(s))

    comment_dictionary = data
    count = 1
    for item in comment_dictionary:
        # print(data)
        if 'author' in item:
            author = item['author']['displayName']
            author_authenticated = item['author']['me']
            author_createdDate = item['createdTime']
            author_modifiedDate = item['modifiedTime']
            content_html = item['htmlContent']
            content_message = item['content']
            is_deleted = item['deleted']
            if len(item['replies']) == 0:
                replied_user = "No replies from student"
                replied_comment = None
                print(link+ " | " +author + " | " + author_createdDate + " | " + content_message + " | " + replied_user)
                print(str(count),". The comment created by |" + author +  "| on " +author_createdDate +  "| and the comment given by author is \"|"  +content_message + "|\". ")
            else:
                for i in range(len(item['replies'])):
                    replied_user = item['replies'][i]['author']['displayName']
                    replied_comment = item['replies'][i]['content']
                    print(link+ " | " +author + " | " + author_createdDate + " | " + content_message + " | " + replied_user)
                    print(str(count),". The comment created by ", author, " on " ,author_createdDate, " and the comment given by author is \"", content_message, "\". This comment is replied by ", replied_user, " on ", author_modifiedDate, " is \"", replied_comment, "\".")
                    count += 1
        else:
            print("Author not found | ", link)

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.readonly']

def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    list_documents = ["https://docs.google.com/document/d/13-Mixv0ioFY_BDdlLhnV2djoJmq0gsVIL80pEf-inTs/edit"]
    for i in list_documents:
        if "docs" in i:
            document_id = i.split("/")[-2]
            try:
                comments = service.comments().list(fileId=document_id,fields="comments",includeDeleted=True).execute()
                read_json(i, comments.get('comments', []))
            except errors.HttpError as error:
                print(i + " | " + "No permissions")

if __name__ == '__main__':
    main()