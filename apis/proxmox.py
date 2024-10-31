import requests
import json

requests.urllib3.disable_warnings()
api_prefix = "api2/json"

class proxmox:
    @staticmethod
    def _headers(token_id, secret):
        headers = {
            "Authorization": f"PVEAPIToken={token_id}={secret}"
        }
        return headers

    @staticmethod
    def _path_normalize(api_path):
        api_path = api_path.rstrip('/')
        if not api_path.endswith("/"):
            api_path += "/"
        return api_path
    
    # this helper function for proxmox is used to keep api calls in a main function generic
    @staticmethod
    def mk_api_base(config):
        if config["token_id"] is None:
            raise ValueError("proxmox: api token not found in JSON file")
        if config["secret"] is None:
            raise ValueError("proxmox: api secret not found in JSON file")
        if config["api_address"] is None:
            raise ValueError("proxmox: api_address not found in JSON file")
        api_base = []
        # enshure, that the content of api_base has the correct order!
        api_base.append(config['api_address'])
        api_base.append(config['token_id'])
        api_base.append(config['secret'])

        return api_base

    @staticmethod
    def get(api_address, token_id, secret, api_path):

        api_path = proxmox._path_normalize(api_path)
        headers = proxmox._headers(token_id, secret)
        url = f'{api_address}/{api_prefix}/{api_path}'

        response = requests.get(url, headers=headers, verify=False)
        return response

    @staticmethod
    def post(api_address, token_id, secret, api_path, payload):

        api_path = proxmox._path_normalize(api_path)
        headers = proxmox._headers(token_id, secret)
        url = f'{api_address}/{api_prefix}/{api_path}'
        payload = json.loads(payload)

        response = requests.post(url, headers=headers, json=payload)
        return response

    @staticmethod
    def put(api_address, token_id, secret, api_path, payload):

        api_path = proxmox._path_normalize(api_path)
        headers = proxmox._headers(token_id, secret)
        url = f'{api_address}/{api_prefix}/{api_path}'
        payload = json.loads(payload)

        response = requests.put(url, headers=headers, json=payload)
        return response
    
    @staticmethod
    def delete(api_address, token_id, secret, api_path):

        api_path = proxmox._path_normalize(api_path)
        headers = proxmox._headers(token_id, secret)
        url = f'{api_address}/{api_prefix}/{api_path}'

        response = requests.delete(url, headers=headers)
        return response