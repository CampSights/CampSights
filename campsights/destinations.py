# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

from flask import (
    Blueprint, request, url_for, abort, jsonify
)
from campsights.services.ridb_api import RIDB
from campsights.common import sanitize_input_string

bp = Blueprint('destinations', __name__)


@bp.route('/destinations/campgrounds', methods=['GET'])
def get_list_of_campgrounds_in_provided_radius():
    coordinates = {'lat': 40.8169046, 'lng': -73.1231585}
    api = RIDB()
    destinations = api.query_api_for_all_campgrounds_in_radius(coordinates, 50)

    return str(destinations.json())
