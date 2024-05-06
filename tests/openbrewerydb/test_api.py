import pytest
import requests


@pytest.mark.parametrize(["id_", "code"],
                         [("5128df48-79fc-4f0f-8b52-d06be54d0cec", 200), ("9c5a66c8-cc13-416f-a5d9-0a769c87d318", 200)])
def test_get_list_of_breweries(api_brewerydb_client, id_, code):
    response = api_brewerydb_client.get_list_of_breweries()
    assert response.status_code == code
    assert response.headers
    assert response.json()


@pytest.mark.parametrize('id_', ["b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", "34e8c68b-6146-453f-a4b9-1f6cd99a5ada"])
def test_get_single_brewery1(api_brewerydb_client, id_):
    response = api_brewerydb_client.get_single_brewery(id_)
    assert response.status_code
    assert response.headers
    assert response.json()['name'] == "MadTree Brewing 2.0" or response.json()['name'] == "1 of Us Brewing Company"

@pytest.mark.parametrize("per_page", [ 2, 3 ])
def test_get_list_of_breweries(per_page):
    base_url = 'https://api.openbrewerydb.org/v1'
    response = requests.get(
        base_url + f"/breweries/",
        params={'per_page': per_page}
    )
    assert response.status_code
    assert response.headers
    assert response.json()
    assert len(response.json()) == 3 or len(response.json()) == 2
    # assert response.json()[0]['id']

@pytest.mark.parametrize('name', ["MadTree Brewing 2.0"])
def test_get_random_brewery(api_brewerydb_client, name):
    response = api_brewerydb_client.get_random_brewery()
    res = [r['name'] for r in response.json()]
    assert response.status_code
    assert response.headers
    assert response.json()
    assert type(res) == list
    assert res  not in ['MadTree Brewing 2.0', 'Angry Chair Brewing, LLC.', 'Weeping Radish Farm Brewery']


@pytest.mark.parametrize(["predict", "per_page"],
                         [("name", 2)])
def test_get_list_of_breweries2(base_url, predict, per_page):
    response = requests.get(
        base_url + f"/breweries/",
        params={'by_name': predict,
                'per_page': per_page}
    )
    assert response.status_code
    assert response.headers
    assert response.json()
    assert len(response.json()) == 2
    assert response.json()[0]['name']
