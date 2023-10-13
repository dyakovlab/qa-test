import requests


class BaseApi:

    def get(self, url):
        response = requests.get(url)
        return response

    def post(self, url, json):
        response = requests.post(url, json)
        return response

