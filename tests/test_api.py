import requests


BASE_URL = 'https://jsonplaceholder.typicode.com'


def test_get_posts_api():
    response = requests.get(f'{BASE_URL}/posts/1', timeout=10)

    assert response.status_code == 200
    payload = response.json()
    assert payload['id'] == 1
    assert 'title' in payload
    assert 'body' in payload


def test_get_comments_api():
    response = requests.get(f'{BASE_URL}/posts/1/comments', timeout=10)

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 1
