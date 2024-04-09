from quickstart import get_creds, get_service
from pprint import pprint
from dotenv import load_dotenv
import os
import json

load_dotenv()

creds = get_creds()


service = get_service(creds)

file_id = os.getenv("TEST_FILE_ID")


comments = service.comments().list(fileId=file_id, fields="comments").execute()

all_comments = list(comments.get("comments"))
# for  comment  in  comments.get('comments'):
# 	pprint(comment)

print(json.dumps(all_comments, indent=4))
