# Copyright (c) 2018 Matt Carnovale
# This work is available under the "MIT License”.
# Please see the file LICENSE in this distribution
# or license terms.

import os

from flask import Flask

# This is the application factory funtion. This is where any setup,
# configuration, and registration will occur. Here, the Flask app
# is set up to allow for a default development configuration,
# testing configuration, and custom configuration instances. It
# also communicates that the campsights directory exists as a package.


def create_app(test_config=None):
    # Informs the name of the current module & its location
    # Communicates config files are relative to the instance folder
    # (the instance folder holds config data that should not be committed
    # to the repostitory--secrets, db files, etc.)
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # Default key that will be overidden in an instance config
        # Should be random value when deploying
        SECRET_KEY='dev',
        # When you have a database, store it in the instance folder
        DATABASE=os.path.join(app.instance_path, 'campsights.sqlite'),
    )

    if test_config is None:
        # If we are not testing, load the config for the instance
        app.config.from_pyfile('config.py', silent=True)

    else:
        # If a test config has been passed in, load that
        app.config.from_mapping(test_config)

    # Never assume the directory exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # App route to confirm function is working
    @app.route('/')
    def success():
        return 'Small Victory!'

    # Register the blueprints created for app
    from campsights import coordinates
    app.register_blueprint(coordinates.bp)
    from campsights import destinations
    app.register_blueprint(destinations.bp)

    return app
