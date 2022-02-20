import random

import pytest
import requests

DOG_URL = 'https://dog.ceo/api'


def test_all_breeds():
    res = requests.get(DOG_URL + '/breeds/list/all')
    res_json = check_resp(res, 200, 'success')
    assert len(res_json.get('message')) > 0


def test_random_image():
    res = requests.get(DOG_URL + '/breeds/image/random')
    res_json = check_resp(res, 200, 'success')
    assert res_json.get('message') is not None


def test_sub_breeds():
    res_all = requests.get(DOG_URL + '/breeds/list/all')
    res_all_json = check_resp(res_all, 200, 'success')
    breeds = list(res_all_json.get('message').keys())
    i = random.randint(0, len(breeds))
    res_one = requests.get(DOG_URL + '/breed/' + breeds[i] + '/list')
    res_one_json = check_resp(res_one, 200, 'success')
    assert res_one_json.get('message') == res_all_json.get('message')[breeds[i]]


@pytest.mark.parametrize('breed, response_code, response_status',
                         [('clumber', 200, 'success'),
                          ('borzoi', 200, 'success'),
                          ('Breed not found', 404, 'error')])
def test_breed_random_image(breed, response_code, response_status):
    res = requests.get(DOG_URL + '/breed/' + breed + '/images/random')
    res_json = check_resp(res, response_code, response_status)
    assert breed in res_json.get('message')


@pytest.mark.parametrize('breed, response_code, response_status',
                         [('corgi', 200, 'success'),
                          ('germanshepherd', 200, 'success'),
                          ('Breed not found', 404, 'error')])
def test_breed_all_images(breed, response_code, response_status):
    res = requests.get(DOG_URL + '/breed/' + breed + '/images')
    res_json = check_resp(res, response_code, response_status)
    if res_json.get('status') != 'error':
        assert len(res_json.get('message')) > 0
        for i in range(len(res_json.get('message'))):
            assert breed in res_json.get('message')[i]


def check_resp(response, response_code, response_status):
    assert response.status_code == response_code
    res_json = response.json()
    assert res_json.get('status') == response_status
    return res_json
