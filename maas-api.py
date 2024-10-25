import os
import sys
import argparse
import json
import importlib

current_dir = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.join(current_dir, 'apitool-maas')
sys.path.append(project_path)

from api.maas import maas

def main():
    api_type = "maas"
    maas_config = load_api_config(f'{current_dir}/apis.json', api_type)
    maas_chk_cfg(maas_config)

    config_parts = ", ".join(maas_config.values())
    config_list = config_parts.split(", ")

    api_module = importlib.import_module(f"api.{api_type}")
    api_class = getattr(api_module, api_type)

    arg_options = ('-h','--help' ,'--get', '--post', '--put', '--delete')
    
    if len(sys.argv) > 2 and sys.argv[1] in arg_options:
        args = parse_args()
        if args.get:
            config_list.append(args.get)
            response = api_class.get(*config_list)
        
        elif args.post:
            api_path, json_data = args.post
            json_ckeck(json_data)
            config_list.extend([api_path, json_data])
            response = api_class.post(*config_list)

        elif args.put:
            api_path, json_data = args.put
            json_ckeck(json_data)
            config_list.extend([api_path, json_data])
            response = api_class.put(*config_list)

        elif args.delete:
            config_list.append(args.delete)
            response = api_class.delete(*config_list)

    else:
        if len(sys.argv) == 2:
            api_path = sys.argv[1]
            config_list.append(api_path)

            response = api_class.get(*config_list)
        else:
            print("Error: No command or API path provided.")
            sys.exit(1)

    print(response.status_code)
    print(response.text)

def load_api_config(path, api_type):
    try:
        with open(path, 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        sys.exit("Configuration file not found.")
    except json.JSONDecodeError:
        sys.exit("Error decoding the configuration file.")

    config = config["apis"][api_type]
    
    return config

def parse_args():
    parser = argparse.ArgumentParser(description="API Client CLI")
    parser.add_argument('--get', metavar='api_path', help="GET request to API path")
    parser.add_argument('--post', nargs=2, metavar=('api_path', 'json_data'), help="POST request to API path with JSON data")
    parser.add_argument('--put', nargs=2, metavar=('api_path', 'json_data'), help="PUT request to API path with JSON data")
    parser.add_argument('--delete', metavar='api_path', help="DELETE request to API path")

    return parser.parse_args()

def json_ckeck(json_data):
    try:
        json_data = json.loads(json_data)
    except json.JSONDecodeError:
        print("Error: Invalid JSON data.")
        sys.exit(1)

def maas_chk_cfg(maas_config):
    if maas_config["key"] is None:
        raise ValueError("maas: api key not found in JSON file")
    if maas_config["api_address"] is None:
        raise ValueError("maas: api_address not found in JSON file")

if __name__ == "__main__":
    main()