import json

with open('sample.json') as f:
	s = f.read()
	s = s.replace("'","\"")
	data = json.loads(s)

comment_dictionary = data['items']
# print(comment_dictionary)
count = 1
for item in comment_dictionary:
	author = item['author']['displayName']
	author_authenticated = item['author']['isAuthenticatedUser']
	author_createdDate = item['createdDate']
	author_modifiedDate = item['modifiedDate']
	content_html = item['htmlContent']
	content_message = item['content']
	is_deleted = item['deleted']
	status = item['status']
	feedback_word = item['context']['value']
	document_title = item['fileTitle']
	for i in range(len(item['replies'])):
		replied_user = item['replies'][i]['author']['displayName']
		replied_comment = item['replies'][i]['content']
		print(str(count),". The comment created by ", author, " on " ,author_createdDate, " and the comment given by author is \"", content_message, "\". This comment is replied by ", replied_user, " on ", author_modifiedDate, " is \"", replied_comment, "\".")
		count += 1 