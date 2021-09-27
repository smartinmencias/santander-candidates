import requests

response = requests.get('http://192.168.99.106:32000/service/rest/v1/repositories', auth=('admin', 'admin123'))

print (response.text)