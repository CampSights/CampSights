# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

import requests


class Client():
    def __init__(self):
        self.campsights_host = 'http://127.0.0.1:5000'

    def request_list_of_campgrounds_by_zipcode(self, user_request):
        payload = {'zipcode': user_request}
        try:
            location_response = requests.get(self.campsights_host +
                                             '/coordinates/zipcode',
                                             data=payload)
            location_response.raise_for_status()
            location_data = location_response.json()
            payload = {
                'coordinates': location_data['coordinates'], 'radius': 50}
            campgrounds_response = requests.get(self.campsights_host +
                                                '/destinations/campgrounds',
                                                json=payload)
            campgrounds_response.raise_for_status()
            campgrounds_data = campgrounds_response.json()
            destination_response = {}
            destination_response['address'] = location_data['address']
            destination_response['campgrounds'] = campgrounds_data['RECDATA']
            destination_response['metadata'] = campgrounds_data['METADATA']

            return destination_response
        except (Exception, requests.exceptions.HTTPError) as e:
            print('Error: {}'.format(str(e)))
