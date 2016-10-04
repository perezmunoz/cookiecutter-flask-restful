import re
import os
import sys
import json


def check_name():
    """
    Check the names inputted by the user

    Returns
    -------
    void
    """
    MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9\s]+$'

    # List of the names to check
    names_to_check = ['{{ cookiecutter.api_name }}',
                      '{{ cookiecutter.app_name }}']

    for name in names_to_check:
        if not re.match(MODULE_REGEX, name):
            print('ERROR: %s is not a valid Python module name!' % name)

            # Exits with status 1 to indicate failure
            sys.exit(1)


def gen_keys():
    """
    Generate the secret key and the recaptcha public key

    Returns
    -------
    void
    """
    basedir = os.path.abspath(os.path.dirname(__file__))
    cookiecutter_json_path = '/'.join(basedir.split('/')
                                      [:-1] + ['cookiecutter.json'])

    print(basedir)
    print(cookiecutter_json_path)
    print(os.listdir('.'))

    # Load the file
    cookiecutter_json = json.load(open(cookiecutter_json_path, 'rb'))

    # Set the keys
    cookiecutter_json['secret_key'] = os.urandom(40).encode('hex')
    cookiecutter_json['recaptcha_public_key'] = os.urandom(40).encode('hex')

    # Saves back the file
    json.dump(cookiecutter_json, open(cookiecutter_json_path, 'wb'))


check_name()
# gen_keys()
