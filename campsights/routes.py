# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

from flask import (
    Blueprint, request, url_for, abort, g
)
from campsights.services.geocode import Geocode

bp = Blueprint('campsights', __name__)


@bp.route('/test', methods=['GET'])
def testing_geocode_library():
    api = Geocode()
    # returns None if empty string, empty list if invalid search criteria,
    # location if successful
    return api.query_api_for_location_by_name('*&^')
