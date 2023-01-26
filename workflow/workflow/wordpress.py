import requests
import json
import base64

url = 'http://site.local/wp-json/wp/v2'
user = 'adminsite'
password = 'qjII 6bIq q825 ZpKd qWdz iUeC'
creds = user + ':' + password
print(creds)
cred_token = base64.b64encode(creds.encode())
print(cred_token)
header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}
print(header)
post = {
    'title': 'This is WordPress Python Integration Testing',

    'content': 'Hello, this content is published using WordPress Python Integration',
    'status': 'publish',
    'categories': 5,
    'date': '2023-01-05T11:00:00'
}

blog = requests.post(url + '/posts', headers=header, json=post)
print(blog)
