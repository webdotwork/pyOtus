import requests

class DogApi:

    def __init__(self,
                 base_url="https://dog.ceo/api",):
                 # auth_token="special-key"):
        self.session = requests.Session()
        # self.session.headers = {"Authorization": f"{auth_token}",
        #                         "Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url

    def get_list_of_all_breeds(self):
        response = self.session.get(url=f"{self.base_url}/breeds/list/all",)
        return response

    def get_single_brewery(self, id_):
        self.id  = id_
        response = self.session.get(url=f"{self.base_url}/breeds/{self.id}",)
        return response

    def get_random_brewery(self):
        response = self.session.get(url=f"{self.base_url}/breeds/image/random",)
        return response

    # def create_pet(self, data):
    #     response = self.session.post(f"{self.base_url}/pet",
    #                                  json=data)
    #     return response random
