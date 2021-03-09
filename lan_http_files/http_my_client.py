import json
from pprint import pprint
import http.client


HOST = 'localhost'

connection = http.client.HTTPConnection(HOST, port=8080)
connection.request('GET', '/get')

response = connection.getresponse()
body = response.read().decode()
print('Response is:', body)

