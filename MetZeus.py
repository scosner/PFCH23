import requests
import json

# API Endpoint
base_url = 'https://collectionapi.metmuseum.org/public/collection/v1/search'
object_url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects'

# Search Params
params = {'q': 'Greek', 'q':'Classical', 'q':'Attic'}

# request
response = requests.get(base_url, params=params)

# JSON
response_json = json.loads(response.text)

# Limit object amount
object_ids = response_json['objectIDs'][:10]

# empty list
object_data = []

# Loop and get data
for object_id in object_ids:
    object_response = requests.get(f'{object_url}/{object_id}')
    obj = json.loads(object_response.text)
    if obj.get('primaryImageSmall') and obj.get('objectURL'):
        object_data.append(obj)

# HTML table
html = '<html>\n<head>\n<title>The Met - Zeus</title>\n<style>\ntable {\nborder-collapse: collapse;\n}\ntable, th, td {\nborder: 3px solid black;\n}\n</style>\n</head>\n<body>\n<table>\n<tr><th>Image</th><th>Title</th><th>Date</th></tr>\n'
for obj in object_data:
    title = obj.get('title', '')
    artist = obj.get('artistDisplayName', '')
    img_src = obj.get('primaryImageSmall', '')
    object_url = obj.get('objectURL', '')
    object_date = obj.get('objectDate', '')
    html += f'<tr><td><a href="{object_url}"><img src="{img_src}"/></a></td><td>{title}</td><td>{object_date}</td></tr>\n'
html += '</table>\n</body>\n</html>'


# export
with open('MetZeus.html', 'w') as f:
    f.write(html)
