"""base.py: The base test file executed between each of them."""
__author__ = "Girard Alexandre"

from flask_testing import TestCase
from manage import app


class BaseTestCase(TestCase):
    """ Set Base test env for each test case """

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app
