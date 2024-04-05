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
def test_get_list_of_users(api_jsonplaceholder_client, status, code):
    response = api_jsonplaceholder_client.get_list_of_users()
    # json_response = response.json()
    # print(json_response)
    assert response.status_code == code
    # assert json_response

def test_get_list_of_posts(api_jsonplaceholder_client):
    response = api_jsonplaceholder_client.get_list_of_posts()
    # json_response = response.json()
    # print(json_response)
    assert response.status_code
    # assert json_response

def test_post_photo(api_jsonplaceholder_client):
    response = api_jsonplaceholder_client.post_photo(1)
    # json_response = response.json()
    # print(json_response)
    assert response.status_code
    # assert json_response

def test_post_post(api_jsonplaceholder_client):
    response = api_jsonplaceholder_client.post_post()
    # json_response = response.json()
    # print(json_response)
    assert response.status_code
    # assert json_response