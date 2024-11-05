import requests
import json

api_prefix = "service/rest/v1"

class nexus:
    @staticmethod
    def _headers():
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    @staticmethod
    def _path_normalize(api_path):
        api_path = api_path.rstrip('/')
        if not api_path.endswith("/"):
            api_path += "/"
        return api_path
    
    # this helper function for nexus is used to keep api calls in a main function generic
    @staticmethod
    def mk_api_base(config):
        if config["username"] is None:
            raise ValueError("nexus: username not found in JSON file")
        if config["password"] is None:
            raise ValueError("nexus: pqassword not found in JSON file")
        if config["api_address"] is None:
            raise ValueError("nexus: api_address not found in JSON file")
        api_base = []
        # enshure, that the content of api_base has the correct order!
        api_base.append(config['api_address'])
        api_base.append(config['username'])
        api_base.append(config['password'])

        return api_base

    @staticmethod
    def get(api_address, username, password, api_path):

        api_path = nexus._path_normalize(api_path)
        url = f'{api_address}/{api_prefix}/{api_path}'
        headers = nexus._headers()
        response = requests.get(url, headers=headers, auth=(username, password))
        return response

    @staticmethod
    def post(api_address, username, password, api_path, payload):

        api_path = nexus._path_normalize(api_path)

        url = f'{api_address}/{api_prefix}/{api_path}'
        payload = json.loads(payload)
        headers = nexus._headers()
        response = requests.post(url, headers=headers, auth=(username, password), json=payload)
        return response

    @staticmethod
    def put(api_address, username, password, api_path, payload):

        api_path = nexus._path_normalize(api_path)

        url = f'{api_address}/{api_prefix}/{api_path}'
        payload = json.loads(payload)
        headers = nexus._headers()
        response = requests.put(url, headers=headers, auth=(username, password), json=payload)
        return response
    
    @staticmethod
    def delete(api_address, username, password, api_path):

        api_path = nexus._path_normalize(api_path)

        url = f'{api_address}/{api_prefix}/{api_path}'
        headers = nexus._headers()
        response = requests.delete(url, headers=headers, auth=(username, password))
        return response