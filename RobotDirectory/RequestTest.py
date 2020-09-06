import requests
import json
import jsonpath

# parameters = {"lat": 37.78, "lon": -122.41}
# response = requests.get("http://api.open-notify.org/iss-pass.json")
# response = requests.get("http://api.open-notify.org/astros.json")
# response = requests.get("https://jsonplaceholder.typicode.com/users")
response = requests.get("https://reqres.in/api/users/2")
#
# data = response.json()
# print(data)
# print(response.headers)
# print(data[0]["address"]["geo"])
# assert string(81.1496) == data[0]["address"]["geo"]["lng"]
#
#
# send = requests.post("https://jsonplaceholder.typicode.com/users")
# assert 201 == send.status_code

# parse to json
json_resp = json.loads(response.text)
# print(json_resp)
data = jsonpath.jsonpath(json_resp, "data")

# print(data[0])

assert data[0]["id"] == 2, "In correct"

dct = {"name": "morpheus", "job": "leader"}

dct_json = json.dumps(dct)
print(dct_json)

response_post = requests.post("https://reqres.in/api/users", dct_json)

print(response_post.content)
print(response_post.status_code)
print(response_post.headers)
print(response_post.headers.get("Content-Length"))

resp_json = json.loads(response_post.text)
print(resp_json["id"])
