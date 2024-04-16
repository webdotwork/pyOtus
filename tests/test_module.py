# Файл: test_url_status.py

import pytest
import requests

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="URL for testing")
    parser.addoption("--status", type=int, default=200, help="Expected status code for testing")

@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def status(request):
    return request.config.getoption("--status")

def test_valid_url_status(url):
    response = requests.get(url)
    try:
        print(f'headers: {response.headers} \ndata: {response.content} \nstatus: {response.status_code}')
        assert response.status_code == 200
    except AssertionError:
        raise AssertionError(f'status code is!: {response.status_code}')