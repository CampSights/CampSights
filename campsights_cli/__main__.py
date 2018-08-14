# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

# Referenced:
# https://swcarpentry.github.io/python-novice-inflammation/10-cmdline/
# for guidance on creating a command-line-interface

import sys
import common
import campsights_cli.campsights_api


def validate_number_of_args(args):
    if args < 4:
        raise TypeError('\nNot enough arguments provided.'
                        'Requires a command, option and request.\n'
                        'ex:\ncampsights list -z 97217\n'
                        'campsights get --trail Eagle Creek Loop\n')


def validate_command_arg(command):
    if command not in ['camp_list', 'get']:
        raise NameError('\nCommand : {} : not recognized. '
                        'Please choose from: [ camp_list, get ]\n'.format(command))


def validate_option_arg(command, option):
    if command == 'camp_list':
        if option not in ['-z', '--zipcode', '-a', '--address']:
            raise NameError('\nOption : {opt} : not recognized '
                            'for : {cmd} : command. \nPlease choose from: '
                            '[ --zipcode (-z), --address (-a) ]'
                            '\n'.format(opt=option, cmd=command))
    if command == 'get':
        if option not in ['-c', '--camp', '-t', '--trail']:
            raise NameError('\nOption : {opt} : not recognized '
                            'for : {cmd} : command. \nPlease choose from: '
                            '[ --camp (-c), --trail (-t) ]'
                            '\n'.format(opt=option, cmd=command))


def execute_camplist_command(option, user_request):
    campsights_api = campsights_cli.campsights_api.Client()

    if option in ['-z', '--zipcode']:
        try:
            user_request = common.validate_postal_code(user_request)
            campgrounds = \
                campsights_api.request_list_of_campgrounds_by_zipcode(
                    user_request)
        except TypeError as e:
            print(str(e))
            return

    if option in ['-a', '--address']:
        try:
            user_request = common.validate_address_format(user_request)
            campgrounds = \
                campsights_api.request_list_of_campgrounds_by_address(
                    user_request)
        except TypeError as e:
            print(str(e))
            return

    display_up_to_ten_campgrounds(campgrounds)


def display_up_to_ten_campgrounds(campgrounds):
    if campgrounds is not None and campgrounds:
        total = campgrounds['metadata']['RESULTS']['TOTAL_COUNT']
        print('\nLocated {total} results for {address}.\n'.format(
            total=total, address=campgrounds['address']))
        if total > 10:
            print('Here are the first 10:\n')
        for campground in campgrounds['campgrounds']:
            camp_name = campground['FacilityName'].title()
            print('{}'.format(camp_name))
        print()
    else:
        print('Could not locate any campgrounds.')


def main():

    try:
        validate_number_of_args(len(sys.argv))
        command = sys.argv[1].lower()
        option = sys.argv[2].lower()
        user_request = common.sanitize_input_string(
            ' '.join(sys.argv[3:]), True)
        validate_command_arg(command)
        validate_option_arg(command, option)
    except (NameError, TypeError) as e:
        print(str(e))
        return

    if command == 'camp_list':
        execute_camplist_command(option, user_request)


if __name__ == '__main__':
    main()
