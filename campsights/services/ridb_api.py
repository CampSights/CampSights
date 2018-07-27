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

    def query_api_for_all_campgrounds_in_radius(self, coordinates, radius):
        if coordinates and radius:
            lat = 'latitude=' + str(coordinates['lat'])
            lng = 'longitude=' + str(coordinates['lng'])
            rad = 'radius=' + str(radius)
            try:
                # response = requests.get(
                #     self.base_url + 'facilities?' + lat + lng + rad + self.key)
                # return response
                response = requests.get(
                    self.base_url + 'facilities/?query=redrock&apikey='+self.key)
                return response
            except Exception as e:
                print('Error: {}'.format(str(e)))

        return None
