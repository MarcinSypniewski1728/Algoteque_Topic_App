# File with unit tests

import pytest
import json
from app import app

@pytest.fixture
def client():
    '''
    Fixture to set up a test client for the app
    '''
    with app.test_client() as client:
        yield client

def test_calculate_quotes(client):
    '''
    Test to check if quotes are calculated correctly
    '''
    # Define the request data
    request_data = {
        "topics": {
            "reading": 20,
            "math": 50,
            "science": 30,
            "history": 15,
            "art": 10
        }
    }

    # Send a POST request
    response = client.post('/build_quote', json=request_data)

    # Assert the response status code
    assert response.status_code == 200
    response_data = json.loads(response.data)

    # Assert that the response contains the expected provider names
    assert 'provider_a' in response_data
    assert 'provider_b' in response_data
    assert 'provider_c' in response_data

    # Assert the quote values
    assert response_data['provider_a'] == 8.0
    assert response_data['provider_b'] == 5.0
    assert response_data['provider_c'] == 10.0

def test_calculate_quotes_2(client):
    '''
    Test to check if quotes are calculated correctly for a scenario where not all provider's offers match
    '''
    # Define the request data
    request_data = {
        "topics": {
            "reading": 20,
            "history": 15,
            "art": 10
        }
    }

    # Send a POST request
    response = client.post('/build_quote', json=request_data)

    # Assert the response status code
    assert response.status_code == 200
    response_data = json.loads(response.data)

    # Assert that the response contains the expected provider names
    assert 'provider_a' not in response_data
    assert 'provider_b' in response_data
    assert 'provider_c' in response_data

    # Assert the quote values
    assert response_data['provider_b'] == 4.0
    assert response_data['provider_c'] == 3.75

def test_invalid_request_data(client):
    '''
    Test to check if app can handle wrong data
    '''
    # Send an invalid request
    invalid_request_data = {}

    # Send a POST request
    response = client.post('/build_quote', json=invalid_request_data)

    # Assert the response status code for an error
    assert response.status_code == 400

def test_invalid_request_path(client):
    '''
    Test to check if app can handle wrong request path
    '''
    # Define the request data
    request_data = {
        "topics": {
            "reading": 20,
            "history": 15,
            "art": 10
        }
    }

    # Send a POST request
    response = client.post('/not_a_page', json=request_data)

    # Assert the response status code for an error
    assert response.status_code == 404
