# flights.py

from datetime import datetime
import json
import requests
import api_config

#Define parameters to access the public API
params = {
'access_key': api_config.API_KEY,
'limit' : api_config.MAX_RESULTS,
'depIata':'MAD'
}

aircraft = dict()
airline = dict()
arrival = dict()
departure = dict()
flight = dict()
geography = dict()
speed = dict()
status = ""
price = ""


def fetch_json_file():
    """ 
    Fetch a json file as a python dictionary
    """
    api_result = requests.get('https://app.goflightlabs.com/flights', params)
    api_response = api_result.json()
    return api_response


def read_all():
    ls = list(fetch_json_file().values())
    aircraft = ls[1][0]["aircraft"]
    #airline =  ls[1][0]["airline"]
    return ls
