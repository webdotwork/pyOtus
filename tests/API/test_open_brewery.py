import pytest
import requests

BASE_URL = "https://api.openbrewerydb.org/breweries"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.mark.parametrize("brewery_type", ["micro", "nano", "regional", "brewpub", "large"])
def test_breweries_by_type(base_url, brewery_type):
    response = requests.get(f"{base_url}?by_type={brewery_type}")
    assert response.status_code == 200
    for brewery in response.json():
        assert brewery["brewery_type"] == brewery_type

@pytest.mark.parametrize("city", ["San Diego", "Portland", "Austin"])
def test_breweries_by_city(base_url, city):
    response = requests.get(f"{base_url}?by_city={city}")
    assert response.status_code == 200
    for brewery in response.json():
        assert brewery["city"].lower() == city.lower()

@pytest.mark.parametrize("state", ["California", "Texas", "New York"])
def test_breweries_by_state(base_url, state):
    response = requests.get(f"{base_url}?by_state={state}")
    assert response.status_code == 200
    for brewery in response.json():
        assert brewery["state"].lower() == state.lower()

@pytest.mark.parametrize("postal_code", ["44107", "94016", "78701"])
def test_breweries_by_postal_code(base_url, postal_code):
    response = requests.get(f"{base_url}?by_postal={postal_code}")
    assert response.status_code == 200
    for brewery in response.json():
        assert brewery["postal_code"].startswith(postal_code)

@pytest.mark.parametrize("name", ["Cooper", "Lagunitas", "Blue"])
def test_breweries_by_name(base_url, name):
    response = requests.get(f"{base_url}?by_name={name}")
    assert response.status_code == 200
    for brewery in response.json():
        assert name.lower() in brewery["name"].lower()

@pytest.mark.parametrize("per_page", [1, 5, 10])
def test_breweries_pagination(base_url, per_page):
    response = requests.get(f"{base_url}?per_page={per_page}")
    assert response.status_code == 200
    assert len(response.json()) <= per_page

@pytest.mark.parametrize("brewery_id", ["10-barrel-brewing-co-denver", "ale-werks-brewing-company-williamsburg"])
def test_brewery_by_id(base_url, brewery_id):
    response = requests.get(f"{base_url}/{brewery_id}")
    assert response.status_code == 200
    assert response.json()["id"] == brewery_id

@pytest.mark.parametrize("invalid_id", ["unknown-brewery", "invalid-id"])
def test_invalid_brewery_id(base_url, invalid_id):
    response = requests.get(f"{base_url}/{invalid_id}")
    assert response.status_code == 404

@pytest.mark.parametrize("city, state", [
    ("San Diego", "California"),
    ("Austin", "Texas"),
    ("Portland", "Oregon")
])
def test_breweries_by_city_and_state(base_url, city, state):
    response = requests.get(f"{base_url}?by_city={city}&by_state={state}")
    assert response.status_code == 200
    for brewery in response.json():
        assert brewery["city"].lower() == city.lower()
        assert brewery["state"].lower() == state.lower()

@pytest.mark.parametrize("query_param", [
    "by_type=invalidtype",
    "by_city=unknowncity",
    "by_state=unknownstate"
])
def test_invalid_query_params(base_url, query_param):
    response = requests.get(f"{base_url}?{query_param}")
    assert response.status_code == 200
    assert response.json() == []
