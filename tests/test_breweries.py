import random

import pytest
import requests
from geopy import distance
from jsonschema import validate

BREWERY_URL = 'https://api.openbrewerydb.org/breweries'


@pytest.mark.parametrize('qty_per_page', [0, 7, 30, 50, 80, 1000])
def test_breweries_per_page(qty_per_page):
    res_json = requests.get(BREWERY_URL,
                            params={'per_page': qty_per_page}).json()
    if qty_per_page < 50:
        assert len(res_json) == qty_per_page
    else:
        assert len(res_json) == 50


@pytest.mark.parametrize('brewery_type', ['micro', 'large', 'nano', 'closed', 'planning', 'bar'])
def test_breweries_type(brewery_type):
    res_json = requests.get(BREWERY_URL,
                            params={'by_type': brewery_type}).json()
    for element in res_json:
        assert element['brewery_type'] == brewery_type


@pytest.mark.parametrize('city, state, postal',
                         [('san diego', 'California', '5054'), ('san diego', 'California', '00000')])
def test_breweries_several_params(city, state, postal):
    res_json = requests.get(BREWERY_URL,
                            params={'by_city': city, 'by_state': state, 'by_postal': postal}).json()
    for element in res_json:
        assert city.upper() in element['city'].upper()
        assert state.upper() in element['state'].upper()
        assert postal in element['postal_code']


def test_sort_dist():
    x, y = random.uniform(-90, 90), random.uniform(-180, 180)
    res_json = requests.get(BREWERY_URL,
                            params={'by_dist': str(x) + ',' + str(y)}).json()
    min_dist = 0
    for elements in res_json:
        next_dist = distance.distance([x, y], [elements['latitude'], elements['longitude']])
        assert min_dist <= next_dist
        min_dist = next_dist


def test_api_json_schema():
    bar_list = requests.get(BREWERY_URL,
                            params={'per_page': 50}).json()
    res = requests.get(BREWERY_URL + '/' + bar_list[random.randint(0, len(bar_list))]['id']).json()
    schema = {
        'type': 'object',
        'properties': {
            'id': {'type': 'string'},
            'name': {'type': 'string'},
            'brewery_type': {'type': 'string'},
            'street': {'type': 'string'},
            'address_2': {'type': ['string', 'null']},
            'address_3': {'type': ['string', 'null']},
            'city': {'type': 'string'},
            'state': {'type': 'string'},
            'county_province': {'type': ['string', 'null']},
            'postal_code': {'type': 'string'},
            'country': {'type': 'string'},
            'longitude': {'type': ['string', 'null']},
            'latitude': {'type': ['string', 'null']},
            'phone': {'type': ['string', 'null']},
            'website_url': {'type': ['string', 'null']},
            'updated_at': {'type': 'string'},
            'created_at': {'type': 'string'}
        },
        'required': ['id', 'name', 'brewery_type', 'street', 'address_2', 'address_3', 'city', 'state',
                     'county_province',
                     'postal_code', 'country', 'longitude', 'latitude', 'phone', 'website_url', 'updated_at',
                     'created_at']
    }

    validate(instance=res, schema=schema)
