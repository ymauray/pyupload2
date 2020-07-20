from requests.auth import HTTPBasicAuth

import requests
import json

class Service:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def post(self, endpoint, data):
        url = "https://auphonic.com/api/{}.json".format(endpoint)
        data = json.dumps(data) if data is not None else None
        r = requests.post(
                url,
                auth=HTTPBasicAuth(self._username, self._password),
                headers={"content-type": "application/json"},
                data=data
        )

        if r.status_code != 200:
            raise Exception("Error: status code {} for url {}".format(r.status_code, url))

        j = r.json()

        if j["status_code"] != 200:
            raise Exception("Error : staus code = {}".format(j["status_code"]))
        if j["error_code"] is not None:
            raise Exception("Error : code = {}, message = {}".format(j["error_code"], j["error_message"]))

        return j

    def get(self, endpoint):
        url = "https://auphonic.com/api/{}.json".format(endpoint)
        r = requests.get(
            url,
            auth=HTTPBasicAuth(self._username, self._password),
            headers={"content-type": "application/json"}
        )

        if r.status_code != 200:
            raise Exception("Error: status code {} for url {}".format(r.status_code, url))

        j = r.json()

        if j["status_code"] != 200:
            raise Exception("Error : staus code = {}".format(j["status_code"]))
        if j["error_code"] is not None:
            raise Exception("Error : code = {}, message = {}".format(j["error_code"], j["error_message"]))

        return j

    def upload(self, endpoint, files):
        url = "https://auphonic.com/api/{}.json".format(endpoint)
        r = requests.post(
                url,
                auth=HTTPBasicAuth(self._username, self._password),
                files=files
        )

        if r.status_code != 200:
            raise Exception("Error: status code {} for url {}".format(r.status_code, url))

        j = r.json()

        if j["status_code"] != 200:
            raise Exception("Error : staus code = {}".format(j["status_code"]))
        if j["error_code"] is not None:
            raise Exception("Error : code = {}, message = {}".format(j["error_code"], j["error_message"]))

        return j
