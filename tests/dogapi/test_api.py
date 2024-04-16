import json
import pytest
import requests
import cerberus

@pytest.mark.parametrize(["status", "code"],
                         [("available", 200), ("pending", 200), ("sold", 200)])
def test_get_list_of_all_breeds(api_dogsapi_client, status, code):
    response = api_dogsapi_client.get_list_of_all_breeds()
    assert response.status_code == code
    assert response.headers
    assert response.json()
    assert len(response.json()["message"]) != 0
    print(response.json()["message"])
    # breeds = all((response.json()["message"]))
    # return breeds

breeds = ["african", "coco", "akita"]
@pytest.mark.parametrize('breeds', [breeds])
def test_get_single_breed(breeds):
    for breed in breeds:
        print(breed)
        res = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random",)
        assert res.status_code
        assert res.headers
        assert res.json()
        print(res.json())
        if breed == "coco":
            assert res.status_code == 404

schema = {
        # "message": str,
        "status": 'success'
        }

def test_get_random_breed_one(api_dogsapi_client):
    # Verify addition and response
    try:
        response = api_dogsapi_client.get_random_breed()
        assert response.json().get("status") == "success"
    except AssertionError:
        raise AssertionError(response.json())

def test_get_random_breed_two(api_dogsapi_client):
    # Verify addition and response
    try:
        response = api_dogsapi_client.get_random_breed()
        assert response.json() == schema
    except AssertionError:
        raise AssertionError(response.json())
    #

def test_get_list_of_all_breeds2(api_dogsapi_client):
    response = api_dogsapi_client.get_list_of_all_breeds()
    assert response.status_code
    assert response.headers
    assert response.json()
    breeds = all((response.json()["message"]))
    assert breeds

