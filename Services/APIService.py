import requests
from Services.LocalBearerService import LocalBearerService


class APIService:
    def __init__(self, backend_url='http://172.21.40.127:12038'):
        self.backend_url = backend_url
        self.local_service = LocalBearerService()

    def get_headers(self):
        token = self.local_service.get_bearer_token()
        headers = {
            'Content-Type': 'application/json'
        }
        if token:
            headers['Authorization'] = f'Bearer {token}'
        return headers

    def post(self, endpoint, data):
        url = f"{self.backend_url}/{endpoint}"
        headers = self.get_headers()
        print(f"POST request to {url} with headers {headers} and data {data}")
        response = requests.post(url, json=data, headers=headers)
        print(f"Response: {response.status_code} {response.text}")
        return response

    def get(self, endpoint):
        url = f"{self.backend_url}/{endpoint}"
        headers = self.get_headers()
        print(f"GET request to {url} with headers {headers}")
        response = requests.get(url, headers=headers)
        print(f"Response: {response.status_code} {response.text}")
        return response

    def login_user(self, login_url, credentials):
        response = self.post(login_url, credentials)
        if response.status_code == 200:
            bearer_token = response.json().get('token')
            if bearer_token:
                self.local_service.save_bearer_token(bearer_token)
                return True
        return False