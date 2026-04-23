import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        return requests.get(url)
    
    def post(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        return requests.post(url, json = data)