from requests.auth import HTTPBasicAuth

import requests
import json

class Service:
    def __init__(self, endpoint, username, password):
        self._endpoint = endpoint
        self._username = username
        self._password = password

    def post(self, data):
        r = requests.post(
                "https://auphonic.com/api/{}.json".format(self._endpoint),
                auth=HTTPBasicAuth(self._username, self._password),
                headers={"content-type": "application/json"},
                data=json.dumps(data)
        )

        if r.status_code != 200:
            raise Exception("Error: status code = {}".format(r.status_code))

        j = r.json()

        if j["status_code"] != 200:
            raise Exception("Error : staus code = {}".format(j["status_code"]))
        if j["error_code"] is not None:
            raise Exception("Error : code = {}, message = {}".format(j["error_code"], j["error_message"]))

        return j

