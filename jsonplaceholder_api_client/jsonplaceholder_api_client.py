import requests

class JsonPlaceHolder:

    def __init__(self,
                 base_url="https://jsonplaceholder.typicode.com",):
                 # auth_token="special-key"):
        self.session = requests.Session()
        # self.session.headers = {"Authorization": f"{auth_token}",
        #                         "Content-Type": "application/json"}
        self.session.verify = False
        self.base_url = base_url

    def get_list_of_users(self):
        response = self.session.get(url=f"{self.base_url}/users",)
        return response

    def get_list_of_posts(self):
        response = self.session.get(url=f"{self.base_url}/users",)
        return response

    def post_photo(self, id_):
        self.id  = id_
        response = self.session.get(url=f"{self.base_url}/photos/{self.id}",)
        return response

    def post_post(self):
        response = self.session.get(url=f"{self.base_url}/comments",)
        return response

    # def create_pet(self, data):
    #     response = self.session.post(f"{self.base_url}/pet",
    #                                  json=data)
    #     return response random
