import requests
from typing import Optional

class JsonPlaceHolder:

    def __init__(self,
                 base_url="https://jsonplaceholder.typicode.com",):
                 # auth_token="special-key"):
        self.session = requests.Session()
        # self.session.headers = {"Authorization": f"{auth_token}",
        #                         "Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url

    def get_posts(self):
        response = self.session.get(url=f"{self.base_url}/posts",)
        return response

    def get_list_of_posts(self):
        response = self.session.get(url=f"{self.base_url}/users",)
        return response

    def post_post(self, json=None):
        if json is None:
            json = {}
        self.json  = json
        response = self.session.post(url=f"{self.base_url}/posts", json=self.json)
        return response
