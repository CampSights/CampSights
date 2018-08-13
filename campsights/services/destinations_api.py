# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

# The Destinations module utilizes the RIDB & Hiking project APIs
# to serve requests for campgrounds and trails when the client
# hits the endpoints provided in the destinations.py.


import requests
from flask import current_app


class Destinations():
    def __init__(self):
        self.ridb_base_url = 'https://ridb.recreation.gov/api/v1/'
        self.ridb_key = current_app.config['RIDB_KEY']
        self.hiking_project_base_url = 'https://www.hikingproject.com' \
            '/data/get-trails'
        self.hiking_project_key = current_app.config['HIKING_PROJECT_KEY']

    # Consumes RIDB api to retrieve campgrounds within a given radius of
    # a latitude & longitude
    def query_api_for_all_campgrounds_in_radius(self, lat, lng,
                                                radius, limit=10):
        if lat and lng:
            payload = {
                'latitude': lat,
                'longitude': lng,
                'radius': radius,
                'limit': limit,
                'activity': 'camping',
                'apikey': self.ridb_key
            }
            try:
                response = requests.get(
                    self.ridb_base_url + 'facilities/', params=payload)
                return response
            except Exception as e:
                print('Error: {}'.format(str(e)))

        return None

    # Consumes RIDB api to retrieve a specific trail a
    # user has requested. The filters provided by the api are quite
    # limited so the top 20 results are collected and parsed for
    # the requested trail.
    def query_api_for_specified_campground(self, campground_name, state):
        if state and campground_name:
            payload = {
                'query': campground_name,
                'state': state,
                'activity': 'camping',
                'apikey': self.ridb_key
            }
            try:
                response = requests.get(
                    self.ridb_base_url + 'facilities/', params=payload)
                # response = self.parse_result_for_specified_campground(
                # campground_name, response)
                return response
            except Exception as e:
                print('Error: {}'.format(str(e)))

        return None

    # Consumes Hiking Project api to retrieve trails within a
    # given radius of a latitude & longitude
    def query_api_for_all_trails_in_radius(self, lat, lng, radius):
        if lat and lng:
            payload = {
                'lat': lat,
                'lon': lng,
                'maxDistance': radius,
                'key': self.hiking_project_key
            }
            try:
                response = requests.get(
                    self.hiking_project_base_url, params=payload)
                return response
            except Exception as e:
                print('Error: {}'.format(str(e)))

        return None

    # Consumes Hiking Project api to retrieve a specific trail a
    # user has requested. The filters provided by the api are very
    # limited so the top 20 results are collected and parsed for
    # the requested trail.
    def query_api_for_specified_trail(self, lat, lng, trail_name):
        if lat and lng:
            payload = {
                'lat': lat,
                'lon': lng,
                'maxDistance': 1,
                'maxResults': 20,
                'sort': 'distance',
                'key': self.hiking_project_key
            }
            try:
                response = requests.get(
                    self.hiking_project_base_url, params=payload)
                response = self.parse_result_for_specified_trail(
                    trail_name, response)
                return response
            except Exception as e:
                print('Error: {}'.format(str(e)))

        return None

    # Parses the results returned from the query for a specific trail.
    # A dictionary is created in the event that two very similar trails
    # exists in the same location (usually a 'trail' versus 'loop' with
    # the same name). Serving more than one matching result allows the
    # user to select the one they were searching for.
    def parse_result_for_specified_trail(self, trail_name, result):
        trail_results = {}
        if result:
            trails = result.json()
            for trail in trails['trails']:
                if trail_name.lower() in trail['name'].lower():
                    trail_results[trail['name']] = trail

        return trail_results

    # Parses the results returned from the query for a specific campground.
    # The RIDB api will use the query attribute to  filter on facility name,
    # description, keywords, and stay limit. This routine will only return
    # the result with the specified campground name in the facilityName
    # field
    def parse_result_for_specified_campground(self, campground_name, result):
        if result:
            campgrounds = result.json()
            for campground in campgrounds['RECDATA']:
                if campground_name.upper() in campground['FacilityName']:
                    return campground

        return None
