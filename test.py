from quickstart import get_creds, get_service
from pprint import pprint

creds = get_creds()


service  = get_service(creds)

file_id  = input("File id?: ")


file = service.files().get(fileId=file_id).execute()

print(file)
comments  =  service.comments().list(fileId=file_id,fields='comments').execute()            
for  comment  in  comments.get('comments'):                  
	pprint(comment)