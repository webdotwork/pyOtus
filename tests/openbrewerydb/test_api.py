import pytest
from jsonschema import validate
from pyOtus.schemas import schema


@pytest.mark.parametrize(["id", "code"],
                         [("9c5a66c8-cc13-416f-a5d9-0a769c87d318", 200), ("9c5a66c8-cc13-416f--0a769c87d318", 404), ("9c5a66c8-cc13-416f-a5d9-0a769c87d318", 200)])
def test_get_single_brewery_2(api_brewerydb_client, id, code):
    response = api_brewerydb_client.get_single_brewery(id)
    json_response = response.json()
    assert response.status_code == code
    assert json_response
    validate(instance=json_response, schema=schema)


@pytest.mark.parametrize(["status", "code"],
                         [("available", 200), ("pending", 200), ("sold", 200)])
def test_get_list_of_breweries(api_brewerydb_client, status, code):
    response = api_brewerydb_client.get_list_of_breweries()
    json_response = response.json()
    assert response.status_code == code
    assert json_response


@pytest.mark.parametrize(["id", "code"],
                         [("9c5a66c8-cc13-416f-a5d9-0a769c87d318", 200), ("9c5a66c8-cc13-416f-a5d9-00009900", 404), ("34e8c68b-6146-453f-a4b9-1f6cd99a5ada", 200)])
def test_get_single_brewery(api_brewerydb_client, id, code):
    response = api_brewerydb_client.get_single_brewery(id)
    json_response = response.json()
    assert response.status_code == code
    assert json_response


@pytest.mark.parametrize(["id", "code"],
                         [("4e09e7f2-b9c7-4580-8c6a-1241f8835bf9", 200), ("4e09e7f2-b9c7-4580--1241f8835bf9", 200)])
def test_get_random_brewery(api_brewerydb_client, id, code):
    response = api_brewerydb_client.get_random_brewery()
    json_response = response.json()
    assert json_response[0]['id'] != id
    assert response.status_code == code

def test_get_random_brewery_2(api_brewerydb_client):
    response = api_brewerydb_client.get_random_brewery()
    assert response.status_code