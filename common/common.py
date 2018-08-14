# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

# This file will contain utility functions that could
# potentially be used across the application (currency
# conversion, date formatting, etc.)


import re


def sanitize_input_string(user_string, from_main=False):

    if not user_string or user_string is None:
        return ''

    if not from_main:
        # Remove surrounding and duplicate whitespace
        # This strategy was referenced from
        # https://stackoverflow.com/a/8270146
        user_string = ' '.join(user_string.split())

    # Remove any surrounding single quotes
    user_string = user_string.strip('\'')

    # Remove special characters(would like an alternative to regex)
    # The regex used here was constructed using https://regex101.com/
    # It matches all the characters not present in the list.
    user_string = re.sub('[^a-zA-Z0-9 \'#-,.]', '', user_string)

    return user_string

# A feable attempt to ensure that the zipcode entered is at least
# numerical, 5 digits, or the 9 digit dash-separated version that
# specifies a geographic segement within a given zipcode area.


def validate_postal_code(user_request):
    bad_zip_message = '\nError: bad entry for ' \
        'zipcode request.\nShould be a 5 digit ' \
        'code or a 5 digit code plus 4 additional' \
        '\ndigits (dash-separated) to identify a ' \
        'geographic segement\nwithin the zipcode.' \
        '\nex:\n97207\n97207-0751\n'

    zip_without_chars = re.sub('[^0-9-]', '', user_request)

    if len(zip_without_chars.split()) > 1:
        raise TypeError('{}'.format(bad_zip_message))

    zip_segments = zip_without_chars.split('-')
    zip_seg_count = len(zip_segments)
    if zip_seg_count > 2:
        raise TypeError('{}'.format(bad_zip_message))
    if zip_seg_count == 2:
        if len(zip_segments[1]) != 4:
            raise TypeError('{}'.format(bad_zip_message))
    if len(zip_segments[0]) != 5:
        raise TypeError('{}'.format(bad_zip_message))

    return zip_without_chars

# A feable attempt to ensure that the address entered doesn not
# contain digits and consists of a city & state


def validate_address_format(user_request):
    bad_address_message = '\nError: bad entry for ' \
        'partial address request.\nPlease provide a city ' \
        'and state separated by a comma.\n' \
        '\nex: \nPortland, Or\nPortland, Oregon\n'

    address_just_chars = re.sub('[^a-zA-Z ,]', '', user_request)
    address_segements = address_just_chars.split(',')
    address_segements_count = len(address_segements)
    if address_segements_count != 2:
        raise TypeError('{}'.format(bad_address_message))
    if not address_segements[0].strip():
        raise TypeError('{}'.format(bad_address_message))
    if not address_segements[1].strip():
        raise TypeError('{}'.format(bad_address_message))

    return ', '.join(address_segements)
