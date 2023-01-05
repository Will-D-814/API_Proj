import requests
import pytest
from wiremock import WireMock


expected_response_body = {"Test":"Json"}



def test_my_api_call(mocker, url):  # pass url as a parameter
    # Start the wiremock server
    wiremock = WireMock()
    wiremock.start()

     # Set an expectation that the server should receive a GET request
    wiremock.expect_get(url).and_return(status=200, body=expected_response_body)

    # Make the actual API call
    response = requests.get(url)

    # Validate that the response from the API matches the expected response
    assert response.status_code == 200
    assert response.json() == expected_response_body

    # Stop the wiremock server
    wiremock.stop()