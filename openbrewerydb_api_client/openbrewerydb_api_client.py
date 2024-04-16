import requests
from typing import Optional

class OpenBreweryDb:

    def __init__(self,
                 base_url="https://api.openbrewerydb.org/v1",):
                 # auth_token="special-key"):"Authorization": f"{auth_token}",
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url

    def get_list_of_breweries(self):
        response = self.session.get(url=f"{self.base_url}/breweries",)
        return response

    def get_single_brewery(self, id_):
        self.id  = id_
        response = self.session.get(url=f"{self.base_url}/breweries/{self.id}",)
        return response

    def get_random_brewery(self):
        # self.params = params
        response = self.session.get(url=f"{self.base_url}/breweries/random",)
        return response

    # def create_pet(self, data):
    #     response = self.session.post(f"{self.base_url}/pet",
    #                                  json=data)
    #     return response random
