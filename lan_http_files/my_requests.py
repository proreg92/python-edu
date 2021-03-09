from pprint import pprint
import requests


headers = {
    'Content-type': 'application/json',
    'MySecretHeader': 'spam and eggs'
}

data = {
    'MySecretHeader': 'spam and eggs',
    'what?': 42
}

# response = requests.request('GET', 'http://httpbin.org/get')
response1 = requests.get('http://httpbin.org/get')
response2 = requests.post('http://httpbin.org/post', headers=headers)

response3 = requests.post(
    'http://httpbin.org/post',
    headers=headers, json=data
)

response_json = response3.json()

pprint(response1.json())
pprint(response2.json())

print('__________')
pprint(response3.json())
pprint(response_json['json'] == data)