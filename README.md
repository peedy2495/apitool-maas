# apitool-maas

a little api commandline tool to use a rest api - here: maas

## Usage

python3 api.py [-h] [--api API] [--get api_path] [--delete api_path] [--post api_path json_data]
                   [--put api_path json_data]
                   [api_path]

API Client CLI

```text
Options:
  -h, --help                      show the help message and exit
  --api api-name                  specify the target API name. The default is defined in apis.json.
  "--get" [api_path]              GET request to API path; --get is optional; without an option it's always a GET request
  --post [api_path] [json_data]   POST request to API path with JSON data
  --put [api_path] [json_data]    PUT request to API path with JSON data
  --delete [api_path]             DELETE request to API path

positional arguments:
  api_path              Get request for the specified path if no other action specified.

options:
  -h, --help                show the help message and exit
  --api API                 Specify the API name.
  --get api_path            Get request for the specified path.
  --delete api_path         Delete request for the specified path.
  --post api_path json_data Post request for path with JSON data.
  --put api_path json_data  Put request for path with JSON data.
```

## Configuration

Location: `[projectfolder]/apis.json`

Content:

```json
{
    "default_api" : "maas",
    "apis": {
        "maas": {
            "key": "abcdef:ghgijklm:nopqrst",
            "api_address": "http://192.168.0.200:5240"
        },
    }
}
```

## Remarks

This Project will be added to Python's sys.path to be able to use this tool from every place.

Regarding the API path, there is no convention on how to format it:

```text
machines
/machines
machines/
/machines/
```

## Examples

`python3 maas-api.py tags`
or
`python3 maas-api.py --get tags`

`python3 maas-api.py --post tags '{"name":"foo"}'`

`python3 maas-api.py --delete tags/foo`
