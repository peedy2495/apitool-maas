import os
import sys
import argparse
import json
import importlib

current_dir = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.join(current_dir, 'apitool-maas')
sys.path.append(project_path)


def main():

    api_type  = load_default_api(f'{current_dir}/apis.json')

    args = parse_args()

    if args.api:
        api_type = args.api

    config, api_class = load_api(api_type, f'{current_dir}/apis.json')
    api_base = api_class.mk_api_base(config)   

    if args.get or args.api_path:
        api_path = args.get or args.api_path
        api_base.append(api_path)
        response = api_class.get(*api_base)

    elif args.post:
        api_path, json_data = args.post
        json_ckeck(json_data)
        api_base.extend([api_path, json_data])
        response = api_class.post(*api_base)

    elif args.put:
        api_path, json_data = args.put
        json_ckeck(json_data)
        api_base.extend([api_path, json_data])
        response = api_class.put(*api_base)

    elif args.delete:
        api_base.append(args.delete)
        response = api_class.delete(*api_base)

    print(response.status_code)
    try:
        json_data = response.json()
    except json.JSONDecodeError:
        if 200 <= response.status_code <= 299:
            print("Success")
            sys.exit(0)
        else:
            sys.exit("ERROR")
    if not (200 <= response.status_code <= 299):
        print("ERROR")
    print(json.dumps(response.json(), indent=2))

def load_default_api(path):
    try:
        with open(path, 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        sys.exit("Configuration file not found.")
    except json.JSONDecodeError:
        sys.exit("Error decoding the configuration file.")
    
    return config["default_api"]

def load_api(api_type, config_path):
    importlib.import_module(f"apis.{api_type}")
    config = load_api_config(config_path, api_type)

    api_module = importlib.import_module(f"apis.{api_type}")
    api_class = getattr(api_module, api_type)

    return config, api_class

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
    parser = argparse.ArgumentParser(description="A script to handle API operations.")

    parser.add_argument('--api', type=str, help="specify the target API name. The default is defined in apis.json.")

    action_group = parser.add_mutually_exclusive_group(required=True)

    action_group.add_argument('--get', metavar='api_path', type=str, help="Get request for the specified path.")
    action_group.add_argument('api_path', nargs='?', help="Get request for the specified path if no other action specified.")
    action_group.add_argument('--delete', metavar='api_path', type=str, help="Delete request for the specified path.")
    action_group.add_argument('--post', nargs=2, metavar=('api_path', 'json_data'), help="Post request for path with JSON data.")
    action_group.add_argument('--put', nargs=2, metavar=('api_path', 'json_data'), help="Put request for path with JSON data.")

    return parser.parse_args()

def json_ckeck(json_data):
    try:
        json_data = json.loads(json_data)
    except json.JSONDecodeError:
        print("Error: Invalid JSON data.")
        sys.exit(1)

if __name__ == "__main__":
    main()