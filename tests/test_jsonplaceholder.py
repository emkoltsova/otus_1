import random

import pytest
import requests
from jsonschema import validate

JSONPLH_URL = 'https://jsonplaceholder.typicode.com'


def test_list_posts():
    res = requests.get(
        JSONPLH_URL + '/posts/')
    assert len(res.json()) > 0


@pytest.mark.parametrize('title, body, user_id',
                         [('new_title', 'new_body', 3500), ('hi', 'test', 0), ('soooo', 'many....', -888)])
def test_post_create(title, body, user_id):
    res = requests.post(
        JSONPLH_URL + '/posts',
        data={'title': title, 'body': body, 'userId': user_id}).json()
    check_res_body(res, title, body, user_id)


@pytest.mark.parametrize('title, body, user_id',
                         [('update_title', 'update_body', 25), ('jhqgwdjhgs', 'fin', 4), ('very very', '?%^&7g', -35)])
def test_post_update(title, body, user_id):
    post_id = random.randint(1, 101)
    res = requests.put(
        JSONPLH_URL + '/posts/' + str(post_id),
        data={'title': title, 'body': body, 'userId': user_id}).json()
    check_res_body(res, title, body, user_id)
    assert int(res['id']) == post_id


@pytest.mark.parametrize('post_id',
                         [-100, 0, 18, 100, 101])
def test_post_comments(post_id):
    res = requests.get(
        JSONPLH_URL + '/posts/' + str(post_id) + '/comments').json()
    if post_id > 0 and post_id < 101:
        assert len(res) > 0
        for item in res:
            assert item['postId'] == post_id

    else:
        assert res == []


def test_posts_schema():
    res = requests.get(
        JSONPLH_URL + '/posts/' + str(random.randint(1, 101))).json()
    schema = {
        'type': 'object',
        'properties': {
            'userId': {'type': 'number'},
            'id': {'type': 'number'},
            'title': {'type': 'string'},
            'body': {'type': 'string'}
        },
        'required': ['userId', 'id', 'title', 'body']
    }

    validate(instance=res, schema=schema)


def check_res_body(response, tittle, body, user_id):
    assert response['title'] == tittle
    assert response['body'] == body
    assert int(response['userId']) == user_id
