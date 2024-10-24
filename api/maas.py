import requests
import uuid
import time

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
    def get(api_key, api_address, api_path):

        api_path = maas._path_normalize(api_path)
        headers = maas._headers(api_key)
        url = f'{api_address}/MAAS/api/2.0/{api_path}'

        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def post(api_key, api_address, api_path, payload):

        api_path = maas._path_normalize(api_path)
        headers = maas._headers(api_key)
        url = f'{api_address}/MAAS/api/2.0/{api_path}'

        response = requests.post(url, headers=headers, data=payload)
        return response

    @staticmethod
    def put(api_key, api_address, api_path, payload):

        api_path = maas._path_normalize(api_path)
        headers = maas._headers(api_key)
        url = f'{api_address}/MAAS/api/2.0/{api_path}'

        response = requests.put(url, headers=headers, data=payload)
        return response
    
    @staticmethod
    def delete(api_key, api_address, api_path):

        api_path = maas._path_normalize(api_path)
        headers = maas._headers(api_key)
        url = f'{api_address}/MAAS/api/2.0/{api_path}'

        response = requests.delete(url, headers=headers)
        return response