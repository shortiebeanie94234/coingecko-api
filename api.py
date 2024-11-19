from dataclasses import dataclass

import requests


@dataclass
class API:
    url: str
    endpoint: str
    payload: object  # Expects filter_value: [list]

    def __init__(self):
        pass

    def set_endpoint(self, endpoint: str):
        self.endpoint = endpoint


class APIClient(API):
    headers: object
    data: object
    response: object

    def request(self):
        self.response = requests.get(self.url + self.endpoint,
                                 headers=self.headers,
                                 params=self.payload)

    def json(self):
        if self.response.status_code == 200:
            return self.response.json()
        return None
