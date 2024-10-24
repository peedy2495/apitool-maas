import os
import sys
import argparse
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.join(current_dir, 'apitool-maas')
sys.path.append(project_path)

from api.maas import maas

def main():
    try:
        with open(f'{current_dir}/apis.json', 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        sys.exit("Configuration file not found.")
    except json.JSONDecodeError:
        sys.exit("Error decoding the configuration file.")

    maas_config = config["apis"]["maas"]

    if maas_config["key"] is None:
        raise ValueError("key not found in JSON file")
    if maas_config["api_address"] is None:
        raise ValueError("api_address not found in JSON file")

    # Define valid options
    options = ('-h','--help' ,'--get', '--post', '--put', '--delete')

    # Check if there are enough arguments and if the first one is a valid command
    if len(sys.argv) > 1 and sys.argv[1] in options:
        # Set up argparse only if a command is provided
        parser = argparse.ArgumentParser(description="API Client CLI")
        parser.add_argument('--get', metavar='api_path', help="GET request to API path")
        parser.add_argument('--post', nargs=2, metavar=('api_path', 'json_data'), 
                            help="POST request to API path with JSON data")
        parser.add_argument('--put', nargs=2, metavar=('api_path', 'json_data'), 
                            help="PUT request to API path with JSON data")
        parser.add_argument('--delete', metavar='api_path', help="DELETE request to API path")

        # Parse the arguments
        args = parser.parse_args()

        # Handle the GET request if specified
        if args.get:
            response = maas.get(maas_config["key"],maas_config["api_address"], args.get)
        
        # Handle the POST request if specified
        elif args.post:
            api_path, json_data = args.post
            try:
                data = json.loads(json_data)  # Validate JSON
            except json.JSONDecodeError:
                print("Error: Invalid JSON data.")
                sys.exit(1)
            response = maas.post(maas_config["key"],maas_config["api_address"], api_path, data)

        # Handle the PUT request if specified
        elif args.put:
            api_path, json_data = args.put
            try:
                data = json.loads(json_data)  # Validate JSON
            except json.JSONDecodeError:
                print("Error: Invalid JSON data.")
                sys.exit(1)
            response = maas.put(maas_config["key"],maas_config["api_address"], api_path, data)

        # Handle the GET request if specified
        elif args.delete:
            response = maas.delete(maas_config["key"],maas_config["api_address"], args.delete)

    else:
        # No command provided, assume the first argument is an API path
        if len(sys.argv) > 1:
            api_path = sys.argv[1]
            response = maas.get(maas_config["key"],maas_config["api_address"], api_path)
        else:
            # No command or API path provided, print error message
            print("Error: No command or API path provided.")
            sys.exit(1)

    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    main()