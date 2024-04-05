import pytest

# from jsonschema import validate
#
# from schemas import schema


# @pytest.mark.parametrize(["status", "code"],
#                          [("available", 200), ("pending", 200), ("sold", 200)])
# def test_get_pet_by_status(api_client, status, code):
#     query = {"status": status}
#     response = api_client.get_pets_by_status(query)
#     json_response = response.json()
#     assert response.status_code == code
#     assert json_response
#     validate(instance=json_response[0], schema=schema)

@pytest.mark.parametrize(["status", "code"],
                         [("available", 200), ("pending", 200), ("sold", 200)])
def test_get_list_of_all_breeds(api_dogsapi_client, status, code):
    response = api_dogsapi_client.get_list_of_all_breeds()
    json_response = response.json()
    print(json_response)
    assert response.status_code == code
    assert json_response

def test_get_single_brewery(api_dogsapi_client):
    response = api_dogsapi_client.get_single_breeds("b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0")
    json_response = response.json()
    print(json_response)
    assert response.status_code
    assert json_response

def test_get_random_breeds(api_dogsapi_client):
    response = api_dogsapi_client.get_random_breeds()
    # json_response = response.json()
    # print(json_response)
    assert response.status_code
    # assert json_response

def test_get_random_breeds(api_dogsapi_client):
    response = api_dogsapi_client.get_random_breeds()
    # json_response = response.json()
    # print(json_response)
    assert response.status_code
    # assert json_response