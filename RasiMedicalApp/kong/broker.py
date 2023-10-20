import requests


# Script to connect microservices apps with the Kong broker
class Broker:
    def __init__(self):
        self.kong_url = "http://34.31.241.179:8000"

    def get(self, endpoint):
        response = requests.get(f"{self.kong_url}/{endpoint}")
        return response.json()

    def post(self, endpoint, data):
        response = requests.post(f"{self.kong_url}/{endpoint}", json=data)
        return response.json()
