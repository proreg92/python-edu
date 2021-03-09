import json
from pprint import pprint
import http.client

HOST = 'httpbin.org'

connection = http.client.HTTPConnection(HOST, port=80)
connection.request('GET', '/get')

response = connection.getresponse()

# body = response.read().decode()
res = json.loads(response.read().decode())
print(res)
pprint(res)

print('________')

pprint(res['headers'])

# print(response.status, response.reason)

print(type(json.dumps(res['headers'])))

