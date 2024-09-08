import pytest
import requests

BASE_URL = "https://dog.ceo/api"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

def test_list_all_breeds(base_url):
    response = requests.get(f"{base_url}/breeds/list/all")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], dict)

def test_random_image(base_url):
    response = requests.get(f"{base_url}/breeds/image/random")
    assert response.status_code == 200
    assert "https://images.dog.ceo/breeds/" in response.json()["message"]

def test_random_image_by_breed(base_url):
    breed = "hound"
    response = requests.get(f"{base_url}/breed/{breed}/images/random")
    assert response.status_code == 200
    assert f"https://images.dog.ceo/breeds/{breed}/" not in response.json()["message"]

def test_list_all_images_by_breed(base_url):
    breed = "hound"
    response = requests.get(f"{base_url}/breed/{breed}/images")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], list)

def test_list_all_sub_breeds(base_url):
    breed = "hound"
    response = requests.get(f"{base_url}/breed/{breed}/list")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], list)

def test_list_images_by_sub_breed(base_url):
    breed = "hound"
    sub_breed = "afghan"
    response = requests.get(f"{base_url}/breed/{breed}/{sub_breed}/images")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], list)

def test_random_image_by_sub_breed(base_url):
    breed = "hound"
    sub_breed = "afghan"
    response = requests.get(f"{base_url}/breed/{breed}/{sub_breed}/images/random")
    assert response.status_code == 200
    assert f"https://images.dog.ceo/breeds/{breed}-{sub_breed}/" in response.json()["message"]

def test_non_existent_breed(base_url):
    breed = "unknown"
    response = requests.get(f"{base_url}/breed/{breed}/images")
    assert response.status_code == 404
    assert response.json()["status"] == "error"

def test_non_existent_sub_breed(base_url):
    breed = "hound"
    sub_breed = "unknown"
    response = requests.get(f"{base_url}/breed/{breed}/{sub_breed}/images")
    assert response.status_code == 404
    assert response.json()["status"] == "error"

def test_random_image_invalid_breed(base_url):
    breed = "invalidbreed"
    response = requests.get(f"{base_url}/breed/{breed}/images/random")
    assert response.status_code == 404
    assert response.json()["status"] == "error"

def test_random_image_invalid_sub_breed(base_url):
    breed = "hound"
    sub_breed = "invalidsubbreed"
    response = requests.get(f"{base_url}/breed/{breed}/{sub_breed}/images/random")
    assert response.status_code == 404
    assert response.json()["status"] == "error"

def test_invalid_endpoint(base_url):
    response = requests.get(f"{base_url}/invalid-endpoint")
    assert response.status_code == 404
    assert response.json()["status"] == "error"

def test_sub_breed_not_in_list(base_url):
    breed = "hound"
    sub_breed = "invalidsubbreed"
    response = requests.get(f"{base_url}/breed/{breed}/{sub_breed}/list")
    assert response.status_code == 404
    assert response.json()["status"] == "error"

def test_invalid_method(base_url):
    response = requests.post(f"{base_url}/breeds/list/all")
    assert response.status_code == 405

def test_random_image_without_breed(base_url):
    response = requests.get(f"{base_url}/breed//images/random")
    assert response.status_code == 404
    assert response.json()["status"] == "error"

def test_list_all_images_invalid_breed(base_url):
    breed = "invalidbreed"
    response = requests.get(f"{base_url}/breed/{breed}/images")
    assert response.status_code == 404
    assert response.json()["status"] == "error"

def test_random_image_invalid_breed_format(base_url):
    breed = "hound123"
    response = requests.get(f"{base_url}/breed/{breed}/images/random")
    assert response.status_code == 404
    assert response.json()["status"] == "error"

def test_list_all_images_by_sub_breed_invalid_format(base_url):
    breed = "hound"
    sub_breed = "afghan123"
    response = requests.get(f"{base_url}/breed/{breed}/{sub_breed}/images")
    assert response.status_code == 404
    assert response.json()["status"] == "error"

def test_status_field_in_response(base_url):
    response = requests.get(f"{base_url}/breeds/list/all")
    assert response.status_code == 200
    assert "status" in response.json()

def test_message_field_in_response(base_url):
    response = requests.get(f"{base_url}/breeds/list/all")
    assert response.status_code == 200
    assert "message" in response.json()
