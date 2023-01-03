import pytest
import requests
import jsonpath




class test_PincodeApi:

    def __init__(self):
        pass

    def test_pincode_api_verify_content_type(self):

        """we call the get() method in the requests library to perform an HTTP GET call to the specified endpoint,
         and we store the entire response in a variable called response."""

        response = requests.get("http://api.zippopotam.us/us/90210")        # response object
        assert response.headers["Content-Type"] == "application/json"

    def test_pincode_api_verify_status_code(self):
        response = requests.get("http://api.zippopotam.us/us/90210")
        assert response.status_code == 200

    def test_pincode_api_verify_country_code(self):
        response = requests.get("http://api.zippopotam.us/us/90210")
        response_body= response.json()
        assert response_body["country"] == "United States"

    def test_pincode_api_verify_place_name(self):
        response = requests.get("http://api.zippopotam.us/us/90210")
        response_body = response.json()         # extract response body from response object
        assert response_body["places"][0]["place name"] == "Beverly Hills"