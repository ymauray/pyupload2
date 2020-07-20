from requests.auth import HTTPBasicAuth

from . import _service as service

import json
import requests
import sys

class Production:
    """Auphonic production"""
    def __init__(self, data, username, password):
        if username is None or password is None:
            raise Exception("Invalid credentials")
        self._data = data
        self._service = service.Service(username, password)
    
    def set_metadata(self, metadata):
        self._metadata = metadata

    def create(self):
        response = self._service.post("productions", self._data)
        self._uuid = response['data']['uuid']

    def use(self, uuid):
        response = self._service.get("production/{}".format(uuid))
        self._uuid = response['data']['uuid']

    def status(self):
        response = self._service.get("production/{}".format(self._uuid))
        return response['data']['status']

    def add_file(self, path, track = "input_file"):
        if self._uuid is None:
            raise Exception("Not initialized")
        files = {}
        files[track] = open(path, 'rb')
        response = self._service.upload("production/{}/upload".format(self._uuid), files=files)
