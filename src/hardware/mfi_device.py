import requests
from requests import Response


class MfiDevice:
    def __init__(self, device_url: str):
        self.response = None
        self.device_url = device_url
        self.session_sensor = requests.Session()
        self.session_sensor.headers = {'content-type': 'application/json'}

    def get_status(self):
        _url_endpoint = '/sensors'
        try:
            self.response = requests.get(self.device_url + _url_endpoint, timeout=0.1)
            self.response.raise_for_status()
            return self.response
        except requests.exceptions.HTTPError as err:
            print(f'HTTP-Error: {err.response.status_code}')
            return None
        except requests.exceptions.RequestException as err:
            print(f'RequestException: {err}')
            return None




