# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

import requests
from flask import current_app


class Destinations():
    def __init__(self):
        self.ridb_base_url = 'https://ridb.recreation.gov/api/v1/'
        self.ridb_key = current_app.config['RIDB_KEY']
        self.hiking_project_base_url = 'https://www.hikingproject.com/data/get-trails'
        self.hiking_project_key = current_app.config['HIKING_PROJECT_KEY']

    # Consumes RIDB api to retrieve campgrounds within a given radius of
    # a latitude & longitude
    def query_api_for_all_campgrounds_in_radius(self, lat, lng, radius):
        if lat and lng:
            payload = {
                'latitude': lat,
                'longitude': lng,
                'radius': radius,
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

    # Consumes Hiking Project api to retrieve campgrounds within a given radius of
    # a latitude & longitude
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
