from api import APIClient
from config import config


class CoinGeckoAPIClient(APIClient):
    url: str = f"{config['api_url']}"
    headers: object = {"x-cg-demo-api-key": config['api_key']}

    def set_payload(self, payload):
        self.payload = self.prepare_payload(payload)

    @staticmethod
    def prepare_payload(data):
        return {'ids': ','.join(data.__getitem__('coin')), 'vs_currencies': ','.join(data.__getitem__('currency'))}

    def send_request(self):
        self.request()
        return self.json()
