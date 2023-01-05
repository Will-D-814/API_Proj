from server_functions.function_list import category_count, output_of_category,get_API_data
import requests
import pytest

def test_get_API_data(URL):
    # Test if the function returns a dictionary
    assert isinstance(get_API_data(URL), dict)
    # Test if the API call is successful
    assert get_API_data(URL)['status'] == 'success'

def test_API_GET_request_code(url):  # pass url as a parameter
    response = requests.get(url, verify=True)  # set verify to True
    response_body = response.json()
    assert response.status_code == 200
    #To validate API response call is successful (Status 200)
    
def test_API_GET_request_count(url):  # pass url as a parameter
    response = requests.get(url, verify=True)  # set verify to True
    response_body = response.json()
    assert response_body["count"] == 1425
    #To validate the count of the API is 1425

def test_API_category_Animals_count_greater_than_0(url):  # pass url as a parameter
    response = requests.get(url, verify=True)  # set verify to True
    response_body = response.json()
    midstep = response_body['entries']
    counter = category_count('Animals', midstep)
    assert counter > 0

def test_API_category_output_is_list(url):  # rename function
    response = requests.get(url, verify=True)  # set verify to True
    response_body = response.json()
    midstep = response_body['entries']
    type_animals = output_of_category('Animals', midstep)
    assert type(type_animals) == list