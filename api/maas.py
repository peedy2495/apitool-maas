import requests
import uuid
import time
import json

class maas:
    @staticmethod
    def _headers(api_key):
        consumer, token, signature = api_key.split(':')

        nonce = str(uuid.uuid4())
        timestamp = str(int(time.time()))

        headers = {
            "Authorization": f'OAuth oauth_version="1.0", '
                             f'oauth_signature_method="PLAINTEXT", '
                             f'oauth_consumer_key="{consumer}", '
                             f'oauth_token="{token}", '
                             f'oauth_signature="&{signature}", '
                             f'oauth_nonce="{nonce}", '
                             f'oauth_timestamp="{timestamp}"'
        }
        return headers

    @staticmethod
    def _path_normalize(api_path):
        api_path = api_path.rstrip('/')
        if not api_path.endswith("/"):
            api_path += "/"
        return api_path
    
    @staticmethod
    def _maas_chk_cfg(maas_config):
        if maas_config["key"] is None:
            raise ValueError("maas: api key not found in JSON file")
        if maas_config["api_address"] is None:
            raise ValueError("maas: api_address not found in JSON file")
    
    @staticmethod
    def mk_api_base(config):
        maas._maas_chk_cfg(config)

        config_parts = ", ".join(config.values())
        api_base = config_parts.split(", ")

        return api_base

    @staticmethod
    def get(api_address, api_key, api_path):

        api_path = maas._path_normalize(api_path)
        headers = maas._headers(api_key)
        url = f'{api_address}/MAAS/api/2.0/{api_path}'

        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def post(api_address, api_key, api_path, payload):

        api_path = maas._path_normalize(api_path)
        headers = maas._headers(api_key)
        url = f'{api_address}/MAAS/api/2.0/{api_path}'
        payload = json.loads(payload)

        response = requests.post(url, headers=headers, json=payload)
        return response

    @staticmethod
    def put(api_address, api_key, api_path, payload):

        api_path = maas._path_normalize(api_path)
        headers = maas._headers(api_key)
        url = f'{api_address}/MAAS/api/2.0/{api_path}'
        payload = json.loads(payload)

        response = requests.put(url, headers=headers, json=payload)
        return response
    
    @staticmethod
    def delete(api_address, api_key, api_path):

        api_path = maas._path_normalize(api_path)
        headers = maas._headers(api_key)
        url = f'{api_address}/MAAS/api/2.0/{api_path}'

        response = requests.delete(url, headers=headers)
        return response