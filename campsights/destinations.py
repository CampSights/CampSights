# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

# This file provides the endpoints that can be utilized when
# the client requests a list of campgrounds, a list of trails,
# a specified campground, or a specified trail.


from flask import (
    Blueprint, request, url_for, abort, jsonify
)
from campsights.services.destinations_api import Destinations
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

        api = Destinations()
        campgrounds = api.query_api_for_all_campgrounds_in_radius(
            lat, lng, radius, 10)
        if campgrounds is None:
            abort(400, 'Error: Request failed.'
                  'Was a latitude & longitude provided?')

    return campgrounds


@bp.route('/destinations/campground', methods=['GET'])
def get_specified_campground():
    # TODO: client application will uses requests package
    # switch back to request.form once implemented.

    campground_name = sanitize_input_string(
        request.form['campground_name'])
    state = sanitize_input_string(request.form['state'])
    if not campground_name:
        abort(400, 'Error: Missing name of campground to lookup.')
    if not state:
        abort(400, 'Error: Missing state in cooridnates.')

    api = Destinations()
    campground = api.query_api_for_specified_campground(
        campground_name, state)
    if campground is None:
        abort(400, 'Error: Request failed.'
              'Could not find results for specified campground')

    return jsonify(campground)


@bp.route('/destinations/trails', methods=['GET'])
def get_list_of_trails_in_provided_radius():
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
            abort(400, 'Error: Missing latitude in coordinates.')
        if not lng:
            abort(400, 'Error: Missing longitude in cooridnates.')

        api = Destinations()
        trails = api.query_api_for_all_trails_in_radius(
            lat, lng, radius)
        if trails is None:
            abort(400, 'Error: Request failed.'
                  'Was a latitude & longitude provided?')

    return trails


@bp.route('/destinations/trail', methods=['GET'])
def get_specified_trail():
    # TODO: client application will uses requests package
    # switch back to request.form once implemented.

    # coordinates = request.form['coordinates']**
    coordinates = request.json['coordinates']
    if coordinates:
        lat = coordinates['lat']
        lng = coordinates['lng']
        # trail_name = request.form['trail_name']**
        trail_name = sanitize_input_string(request.json['trail_name'])

        if not lat:
            abort(400, 'Error: Missing latitude in coordinates.')
        if not lng:
            abort(400, 'Error: Missing longitude in cooridnates.')
        if not trail_name:
            abort(400, 'Error: Missing name of trail to lookup.')

        api = Destinations()
        trail = api.query_api_for_specified_trail(lat, lng, trail_name)
        if trail is None:
            abort(400, 'Error: Request failed.'
                  'Could not find results for specified trail')

    return jsonify(trail)
