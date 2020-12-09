"""manage.py: The manager of the api, to run the app and execute tests."""
__author__      = "Girard Alexandre"

import os
import unittest

from flask_script import Manager

from app.main import create_app
from app import blueprint

app = create_app(os.getenv('TP_CleanCode_ENV') or 'dev')

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
