# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

import googlemaps
from flask import current_app

# In order to use the radius attribute of the api provided by recreation.gov
# the latitude and longitude of the location are required. The GeoCode module
# utilized the google maps geocode library to collect this data.


class Geocode():
    def __init__(self):
        self.client = googlemaps.Client(key=current_app.config['GEO_KEY'])

    def query_api_for_location_by_zipcode(self, zipcode):
        if zipcode or zipcode is not None:
            try:
                geocode_result = self.client.geocode(zipcode)
                return str(parse_location_for_coordinates(geocode_result))
            except Exception as e:
                print('Error: {}'.format(str(e)))

        return None

    def query_api_for_location_by_name(self, name):
        if name or name is not None:
            try:
                geocode_result = self.client.geocode(name)
                return str(parse_location_for_coordinates(geocode_result))
            except Exception as e:
                print('Error: {}'.format(str(e)))

        return 'None'

    def parse_location_for_coordinates(self, result):
        return str(result2[0]['geometry']['location'])
