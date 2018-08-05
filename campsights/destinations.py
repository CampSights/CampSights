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
    # TODO: client application will uses requests package
    # switch back to request.form once implemented.

    # coordinates = request.form['coordinates']**
    coordinates = request.json['coordinates']
    if coordinates:
        lat = coordinates['lat']
        lng = coordinates['lng']
        # radius = request.form['radius']**
        radius = request.json['radius']
        if not lat:
            abort(400, 'Error: Missing latitude in cooridnates.')
        if not lng:
            abort(400, 'Error: Missing longitude in cooridnates.')

        api = RIDB()
        destinations = api.query_api_for_all_campgrounds_in_radius(
            lat, lng, radius)
        if destinations is None:
            abort(400, 'Error: Request failed.'
                  'Was a latitude & longitude provided?')

    return destinations
