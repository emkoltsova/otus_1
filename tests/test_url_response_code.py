import requests


def test_response_code(base_url, resp_code):
    res = requests.get(base_url)
    assert res.status_code == int(resp_code)
