import requests

session = requests.Session()

# session.headers = {"Authorization": "special-key"}
session.verify = False

response = session.get("https://api.openbrewerydb.org/v1/breweries/")
# response = session.post("https://petstore.swagger.io/v2/pet", json={
#         "name": "doggie",
#         "photoUrls": []
#     })
print(response.text)



