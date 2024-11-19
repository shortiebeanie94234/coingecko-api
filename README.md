# Python CoinGecko API plugin

Simple Python OOP CoinGecko API plugin

## Usage

```
api = CoinGeckoAPIClient()
api.set_endpoint('simple/price')
api.set_payload({'coin': ['bitcoin'], 'currency': ['usd']})
response = api.send_request()
print(response)
```