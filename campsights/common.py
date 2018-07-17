# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.


import re


def sanitize_input_string(user_string):

    if not user_string or user_string is None:
        return ''

    # Remove surrounding and duplicate whitespace
    user_string = " ".join(user_string.split())

    # Remove any surrounding single quotes
    user_string = user_string.strip('\'')

    # Remove special characters(would like an alternative to regex)
    user_string = re.sub('[^a-zA-Z0-9_ \']', '', user_string)

    return user_string
