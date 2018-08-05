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


@bp.route('/coordinates/name', methods=['GET'])
def get_coordinates_by_name():
    city = sanitize_input_string(request.form['city'])
    state = sanitize_input_string(request.form['state'])

    if not city:
        abort(400, 'Please provide a *city* and state.')

    if not state:
        abort(400, 'Please provide a city and *state*.')

    api = Geocode()
    name = "{0}, {1}".format(city, state)
    geoData = api.query_api_for_coordinates_by_name(name)

    if geoData is None:
        abort(400, 'Error: Request failed was a city & state provided?')

    return jsonify(geoData)


@bp.route('/coordinates/zipcode', methods=['GET'])
def get_coordinates_by_zipcode():
    zipcode = sanitize_input_string(request.form['zipcode'])

    if not zipcode:
        abort(400, 'Please provide a zipcode.')

    api = Geocode()
    geoData = api.query_api_for_coordinates_by_zipcode(zipcode)

    if geoData is None:
        abort(400, 'Error: Request failed was a zipcode provided?')

    return jsonify(geoData)
