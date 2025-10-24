import requests


class MfiDevice:
    def __init__(self, device_url: str):
        self.device_url = device_url

    # get standard information of the connected device
    def get_status(self):
        _url = '/sensors'
        try:
            header = {'accept': 'application/json'}
            response = requests.get(self.device_url + _url, headers=header)
            response.raise_for_status()
            return response

        except requests.exceptions.HTTPError as err:
            print(f'HTTP-Error: {err}')
        except requests.exceptions.RequestException as err:
            print(f'RequestException: {err}')


