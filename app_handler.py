##Kevin Chen  ID: 49859223

import json
import urllib.request
import urllib.parse


MAPQUEST_KEY = 'Fmjtd|luurn96tn1,aw=o5-9w8wua'

MAPQUEST_URL = 'http://open.mapquestapi.com/directions/v2'


def build_url(start_location: str, end_location: [str])-> str:
    '''takes a starting location and a list of multiple locations for the
    legs of the trip and outputs a mapquest url'''

    query_parameters = [        
        ('key', MAPQUEST_KEY),('from', start_location)       
    ]

    for location in end_location:
        query_parameters.append(('to',location))

        
    return MAPQUEST_URL + '/route?' + urllib.parse.urlencode(query_parameters)


def get_result(url: str)-> 'json':
    '''takes the url from build_url and generates json from it'''

    response = None

    try:
        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')
        return json.loads(json_text)

    finally:
        if response != None:
            response.close()


def _generate_json(start_location: str, end_locations: str)-> 'json':
    '''take in the url and return the json file that it retrieves'''
    
    url = build_url(start_location,end_locations)
    result = get_result(url)

    return result

