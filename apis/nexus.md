# Nexus-UI API-handler module descrition

## Available functions

### `mk_api_base(config)`

`config` is a dict value containing `api_address`, `username` and `password`  
This function is a helper to keep api calls in a main function e.g. apihandler.py generic.  
Return value is a list of `config`-values in the correct order.

### `get(api_address, username, password, api_path)`

Send a get-request to the target API

### `post(api_address, username, password, api_path, payload)`

Send a post-request to the target API with content  
`payload` has to be in a correct json format as string

### `put(api_address, username, password, api_path, payload)`

Send a put-request to the target API with content  
`payload` has to be in a correct json format as string

### `delete(api_address, username, password, api_path)`

Send a delete-request to the target API

## Config for using apihandler.py or 3rd party calls using apis.json

```json
{
    "default_api" : "nexus",
    "apis": {
        "nexus": {
            "api_address": "https://192.168.0.100:8081",
            "username": "foo",
            "password": "mySecretPassword"
        }
    }
}
```

## API reference

The running Nexus instance provides the current API-reference, itself.  
You can reach the API-reference in the webUI under `Setup/Administration/System/API`

**Official website:** 
[https://help.sonatype.com/en/rest-and-integration-api.html](https://help.sonatype.com/en/rest-and-integration-api.html)
