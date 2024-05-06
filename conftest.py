import pytest

from pyOtus.openbrewerydb_api_client.openbrewerydb_api_client import OpenBreweryDb
from pyOtus.jsonplaceholder_api_client.jsonplaceholder_api_client import JsonPlaceHolder
from pyOtus.dog_api_client.dog_api_client import DogApi
def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://api.openbrewerydb.org/v1",
        choices=["https://dog.ceo/api", "https://jsonplaceholder.typicode.com"],
        help="This is request url"
    )

    parser.addoption(
        "--token",
        help="token to authorize",

    )




@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")
    # if is_production_environment():
    #     return chosen_url  # Return the chosen URL
    # elif some_condition():
    #     return "https://dog.ceo/api/breeds"  # Return one URL
    # else:
    #     return "https://petstore.swagger.io/v1"  # Return the other URL
#
@pytest.fixture
def token(request):
    return request.config.getoption("--token")


@pytest.fixture(scope="function")
def api_brewerydb_client(base_url):
    client = OpenBreweryDb(base_url=base_url)
    return client

@pytest.fixture(scope="function")
def api_jsonplaceholder_client(base_url):
    client = JsonPlaceHolder(base_url=base_url)
    return client

@pytest.fixture(scope="function")
def api_dogsapi_client(base_url):
    client = DogApi(base_url=base_url)
    return client