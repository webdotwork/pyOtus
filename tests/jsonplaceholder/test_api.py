import pytest
import requests


@pytest.mark.parametrize(["_id", "code"],
                         [(1, 200), ("1", 200), (1, 200)])
def test_get_posts(api_jsonplaceholder_client, _id, code):
    response = api_jsonplaceholder_client.get_posts()
    assert response.status_code == code
    assert response.headers
    assert response.json()

user_ids = [i for i in range(2)]
props = ['userId', 'id', 'title', 'body']

@pytest.mark.parametrize(["users", "prop"],
                         [(user_ids, props)])
def test_get_posts2(api_jsonplaceholder_client, users, prop):
    response = api_jsonplaceholder_client.get_posts()
    for d in [d for d in response.json()]:
        if d['userId'] in users:
            assert prop[0], prop[1] in d
    assert response.status_code
    assert response.headers
    assert response.json()

def test_post(api_jsonplaceholder_client):
    response = api_jsonplaceholder_client.post_post()
    assert response.status_code
    assert response.headers
    assert response.json()
    return response.json()

json = {
    'title': 'foo',
    'body': 'bar',
    'userId': 654,
}
@pytest.mark.parametrize(["title", "body", "userId"],
                         [(json)])
def test_post2(base_url, title, body, userId):
    response = requests.post(f"https://jsonplaceholder.typicode.com/posts", json=json)
    assert response.status_code
    assert response.headers
    assert response.json()


def test_post_post(api_jsonplaceholder_client):
    data = test_post(api_jsonplaceholder_client)
    d = [d for d in api_jsonplaceholder_client.get_posts().json()]
    for k in d:
        if k.keys() == 'id':
            try:
                assert data['id'] in k.values(k.keys())
            except AssertionError:
                raise AssertionError(api_jsonplaceholder_client.get_posts().json())