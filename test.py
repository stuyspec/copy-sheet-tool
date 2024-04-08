from quickstart import get_creds, get_service
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()

creds = get_creds()


service  = get_service(creds)

file_id  = os.getenv("TEST_FILE_ID")


file = service.files().get(fileId=file_id).execute()

print(file)
comments  =  service.comments().list(fileId=file_id,fields='comments').execute()            
for  comment  in  comments.get('comments'):                  
	pprint(comment)