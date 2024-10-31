import requests
import json

api_prefix = "api"

class semaphore:
    @staticmethod
    def _headers(api_token):
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_token}"
        }
        return headers

    @staticmethod
    def _path_normalize(api_path):
        api_path = api_path.rstrip('/')
        if not api_path.endswith("/"):
            api_path += "/"
        return api_path
    
    # this helper function for semaphore is used to keep api calls in a main function generic
    @staticmethod
    def mk_api_base(config):
        if config["token"] is None:
            raise ValueError("semaphore: api token not found in JSON file")
        if config["api_address"] is None:
            raise ValueError("semaphore: api_address not found in JSON file")
        api_base = []
        # enshure, that the content of api_base has the correct order!
        api_base.append(config['api_address'])
        api_base.append(config['token'])

        return api_base

    @staticmethod
    def get(api_address, api_token, api_path):

        api_path = semaphore._path_normalize(api_path)
        headers = semaphore._headers(api_token)
        url = f'{api_address}/{api_prefix}/{api_path}'

        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def post(api_address, api_token, api_path, payload):

        api_path = semaphore._path_normalize(api_path)
        headers = semaphore._headers(api_token)
        url = f'{api_address}/{api_prefix}/{api_path}'
        payload = json.loads(payload)

        response = requests.post(url, headers=headers, json=payload)
        return response

    @staticmethod
    def put(api_address, api_token, api_path, payload):

        api_path = semaphore._path_normalize(api_path)
        headers = semaphore._headers(api_token)
        url = f'{api_address}/{api_prefix}/{api_path}'
        payload = json.loads(payload)

        response = requests.put(url, headers=headers, json=payload)
        return response
    
    @staticmethod
    def delete(api_address, api_token, api_path):

        api_path = semaphore._path_normalize(api_path)
        headers = semaphore._headers(api_token)
        url = f'{api_address}/{api_prefix}/{api_path}'

        response = requests.delete(url, headers=headers)
        return response