from requests.auth import HTTPBasicAuth

from . import _service as service

import requests
import json

class Production:
    """Auphonic production"""
    def __init__(self, preset = None, multitrack = False, username = None, password = None):
        if username is None or password is None:
            raise Exception("Invalid credentials")

        self._service = service.Service("productions", username, password)

        if preset is not None:
            self._preset = preset
        else:
            raise Exception("Not implemented yet")

    def create(self):
        if self._preset is not None:
            response = self._service.post({
                "preset" : self._preset,
                "metadata": {
                    "title": "PyUpload2 test"
                }
            })

        print(response)

