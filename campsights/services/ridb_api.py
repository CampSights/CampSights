# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

import requests
from flask import current_app


class RIDB():
    def __init__(self):
        self.base_url = 'https://ridb.recreation.gov/api/v1/'
        self.key = current_app.config['RIDB_KEY']

    def query_api_for_all_campgrounds_in_radius(self, lat, lng, radius):
        if lat and lng:
            payload = {
                'latitude': lat,
                'longitude': lng,
                'radius': radius,
                'activity': 'camping',
                'apikey': self.key
            }
            try:
                response = requests.get(
                    self.base_url + 'facilities/', params=payload)
                return response
            except Exception as e:
                print('Error: {}'.format(str(e)))

        return None

    def verify_lat_and_lng_exist(self, coordinates):
        if coordinates['lat'] and coordinates['lng']:
            return true

        return false
