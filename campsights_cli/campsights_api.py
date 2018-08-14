# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

import requests


class Client():
    def __init__(self):
        self.campsights_host = 'http://127.0.0.1:5000'

    def request_list_of_campgrounds_by_zipcode(self, user_request):
        coord_payload = {'zipcode': user_request}
        try:
            geo_response = requests.get(self.campsights_host +
                                        '/coordinates/zipcode',
                                        data=coord_payload)
            geo_response.raise_for_status()
            geo_data = geo_response.json()
            dest_payload = {
                'coordinates': geo_data['coordinates'], 'radius': 50}
            campgrounds_response = requests.get(self.campsights_host +
                                                '/destinations/campgrounds',
                                                json=dest_payload)
            campgrounds_response.raise_for_status()
            campgrounds_data = campgrounds_response.json()

            response = self.format_campgrounds_list_response(
                geo_data, campgrounds_data)

        except (Exception, requests.exceptions.HTTPError) as e:
            print('Error: {}'.format(str(e)))
            return None

        return response

    def request_list_of_campgrounds_by_address(self, user_request):
        city_and_state = user_request.split(',')
        city = city_and_state[0]
        state = city_and_state[1]
        coord_payload = {'city': city, 'state': state}
        try:
            geo_response = requests.get(self.campsights_host +
                                        '/coordinates/partial_address',
                                        data=coord_payload)
            geo_response.raise_for_status()
            geo_data = geo_response.json()
            dest_payload = {
                'coordinates': geo_data['coordinates'], 'radius': 50}
            campgrounds_response = requests.get(self.campsights_host +
                                                '/destinations/campgrounds',
                                                json=dest_payload)
            campgrounds_response.raise_for_status()
            campgrounds_data = campgrounds_response.json()

            response = self.format_campgrounds_list_response(
                geo_data, campgrounds_data)

        except (Exception, requests.exceptions.HTTPError) as e:
            print('Error: {}'.format(str(e)))
            return None

        return response

    def format_campgrounds_list_response(self, geo_data, campgrounds_data):
        destination_response = {}
        destination_response['address'] = geo_data['address']
        destination_response['campgrounds'] = campgrounds_data['RECDATA']
        destination_response['metadata'] = campgrounds_data['METADATA']
        return destination_response
