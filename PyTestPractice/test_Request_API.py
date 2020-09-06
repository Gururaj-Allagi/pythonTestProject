import requests
import json
import jsonpath


def test_getAPI():
    response = requests.get("https://reqres.in/api/users/2")

    # parse to json
    json_resp = json.loads(response.text)
    # print(json_resp)
    data = jsonpath.jsonpath(json_resp, "data")

    # print(data[0])

    assert data[0]["id"] == 2, "In correct"

    dct = {"name": "morpheus", "job": "leader"}

    dct_json = json.dumps(dct)
    print(dct_json)

    response_post = requests.post(".3", dct_json)

    print(response_post.content)
    print(response_post.status_code)
    print(response_post.headers)
    print(response_post.headers.get("Content-Length"))

    resp_json = json.loads(response_post.text)
    print(resp_json["id"])
