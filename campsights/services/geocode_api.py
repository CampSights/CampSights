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

    def query_api_for_coordinates_by_zipcode(self, zipcode):
        if zipcode or zipcode is not None:
            try:
                geocode_result = self.client.geocode(zipcode)
                return self.parse_for_address_and_coordinates(geocode_result)
            except Exception as e:
                print('Error: {}'.format(str(e)))

        return None

    def query_api_for_coordinates_by_name(self, name):
        if name or name is not None:
            try:
                geocode_result = self.client.geocode(name)
                return self.parse_for_address_and_coordinates(geocode_result)
            except Exception as e:
                print('Error: {}'.format(str(e)))

        return None

    def parse_for_address_and_coordinates(self, result):
        return {'address': self.parse_result_for_formatted_address(result),
                'coordinates': self.parse_result_for_coordinates(result)
                }

    def parse_result_for_coordinates(self, result):
        if result:
            return result[0]['geometry']['location']

        return result

    def parse_result_for_formatted_address(self, result):
        if result:
            return result[0]['formatted_address']

        return result
