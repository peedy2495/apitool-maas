# Maas API-handler module descrition

## Available functions

### `mk_api_base(config)`

`config` is a dict value containing `api_address` and `key`  
This function is a helper to keep api calls in a main function e.g. apihandler.py generic.  
Return value is a list of `config`-values in the correct order.

### `get(api_address, api_key, api_path)`

Send a get-request to the target API

### `post(api_address, api_key, api_path, payload)`

Send a post-request to the target API with content  
`payload` has to be in a correct json format as string

### `put(api_address, api_key, api_path, payload)`

Send a put-request to the target API with content  
`payload` has to be in a correct json format as string

### `delete(api_address, api_key, api_path)`

Send a delete-request to the target API

## Config for using apihandler.py or 3rd party calls using apis.json

```json
{
    "default_api" : "maas",
    "apis": {
        "maas": {
            "api_address": "http://192.168.0.100:5240",
            "key": "abcdef:ghijk:lmnopqrst"
        }
    }
}
```

## API reference

[https://maas.io/docs/api](https://maas.io/docs/api)
