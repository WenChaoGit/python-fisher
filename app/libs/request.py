import requests


class Http:

    @staticmethod
    def get(url, response_format='json'):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if response_format == 'json' else ''
        else:
            return r.json() if response_format == 'json' else r.text
