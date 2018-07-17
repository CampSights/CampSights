# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

from flask import (
    Blueprint, request, url_for, abort, jsonify
)
from campsights.services.geocode_api import Geocode
from campsights.common import sanitize_input_string

bp = Blueprint('coordinates', __name__)


@bp.route('/coordinates/name', methods=['GET', 'POST'])
def get_coordinates_by_name():
    if request.method == 'POST':
        city = sanitize_input_string(request.form['city'])
        state = sanitize_input_string(request.form['state'])

        if not city:
            abort(400, 'Please provide a city and state. 1')

        if not state:
            abort(400, 'Please provide a city and state. 2')

        api = Geocode()
        name = "{0}, {1}".format(city, state)
        coordinates = api.query_api_for_coordinates_by_name(name)

        if coordinates is None:
            abort(400, 'Please provide a city and state. 3')

        return jsonify(coordinates)


@bp.route('/coordinates/zipcode', methods=['GET', 'POST'])
def get_coordinates_by_zipcode():
    if request.method == 'POST':
        zipcode = sanitize_input_string(request.form['zipcode'])

        if not zipcode:
            abort(400, 'Please provide a zipcode.')

        api = Geocode()
        coordinates = api.query_api_for_coordinates_by_zipcode(zipcode)

        if coordinates is None:
            abort(400, 'Please provide a zipcode.')

        return jsonify(coordinates)
