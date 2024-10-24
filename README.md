# apitool-maas

a little api commandline tool to use the maas rest api

## Usage:

python3 maas-api.py [-h] [--get api_path] [--post api_path json_data] [--put api_path json_data] [--delete api_path]

API Client CLI

```
Options:
  -h, --help                      show the help message and exit
  "--get" [api_path]              GET request to API path; --get is optional; without an option it's always a GET request
  --post [api_path] [json_data]   POST request to API path with JSON data
  --put [api_path] [json_data]    PUT request to API path with JSON data
  --delete [api_path]             DELETE request to API path
```

## Configuration

Location: `[projectfolder]/apis.json`

Content:

```
{
    "apis": {
        "maas": {
            "key": "abcdef:ghgijklm:nopqrst",
            "api_address": "http://192.168.0.200:5240"
        },
    }
}
```

## Remarks:

This Project will be added to Python's sys.path to be able to use this tool from every place.

Regarding the API path, there is no convention on how to format it:

```
machines
/machines
machines/
/machines/
```

## Examples:

`python3 maas-api.py tags`
or
`python3 maas-api.py --get tags`

`python3 maas-api.py --post tags '{"name":"foo"}'`

`python3 maas-api.py --delete tags/foo`
