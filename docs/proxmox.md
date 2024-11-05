# Proxmox-UI API-handler module descrition

## Available functions

### `mk_api_base(config)`

`config` is a dict value containing `api_address`, `token_id` and `secret`  
This function is a helper to keep api calls in a main function e.g. apihandler.py generic.  
Return value is a list of `config`-values in the correct order.

### `get(api_address, token_id, secret, api_path)`

Send a get-request to the target API

### `post(api_address, token_id, secret, api_path, payload)`

Send a post-request to the target API with content  
`payload` has to be in a correct json format as string

### `put(api_address, token_id, secret, api_path, payload)`

Send a put-request to the target API with content  
`payload` has to be in a correct json format as string

### `delete(api_address, token_id, secret, api_path)`

Send a delete-request to the target API

## Config for using apihandler.py or 3rd party calls using apis.json

```json
{
    "default_api" : "proxmox",
    "apis": {
        "proxmox": {
            "api_address": "https://192.168.0.100:8006",
            "token_id": "user@pam!my-api-token",
            "secret": "abcdef-ghijh-klmn-opqr-stuvxyz"
        }
    }
}
```

## API reference

[https://pve.proxmox.com/pve-docs/api-viewer](https://pve.proxmox.com/pve-docs/api-viewer/index.html)
