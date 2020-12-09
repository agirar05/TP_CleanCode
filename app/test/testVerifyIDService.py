"""testVerifyIDService.py: All the unit test for verify_id_service functions."""
__author__ = "Girard Alexandre"

import unittest

from app.test.base import BaseTestCase

# Import all functions to be tested
from app.main.service.verify_id_service import is_id_valid, check_id, alpha_corresponds_to_total


# Tests for function 'is_id_valid'
class TestIDValidator(BaseTestCase):
    def test_good_id(self):
        """ Test for checking good id """
        good_id1 = "J123456789"
        good_id2 = "Z009999999"
        self.assertEqual(is_id_valid(good_id1), True)
        self.assertEqual(is_id_valid(good_id2), True)

    def test_bad_id(self):
        """ Test for checking bad id - numbers not corresponding to letter """
        bad_id1 = "A123456789"
        bad_id2 = "Z023456789"
        self.assertEqual(is_id_valid(bad_id1), False)
        self.assertEqual(is_id_valid(bad_id2), False)

    def test_id_bad_length(self):
        """ Test for checking bad length id """
        id_too_long = "A1234567890"
        id_too_short = "Z02345678"
        id_empty = ""
        self.assertEqual(is_id_valid(id_too_long), False)
        self.assertEqual(is_id_valid(id_too_short), False)
        self.assertEqual(is_id_valid(id_empty), False)

    def test_key_is_not_letter(self):
        """ Test for checking id with no letter or no number """
        id_no_letter = "0123456789"
        id_no_number = "AZERTISKJC"
        self.assertEqual(is_id_valid(id_no_letter), False)
        self.assertEqual(is_id_valid(id_no_number), False)

    def test_key_is_lowercase(self):
        """ Test for checking id with letter in lowercase """
        good_letter_but_lowercase = "j123456789"
        bad_letter_lowercase = "a123456789"
        self.assertEqual(is_id_valid(good_letter_but_lowercase), False)
        self.assertEqual(is_id_valid(bad_letter_lowercase), False)

    def test_id_with_special_char(self):
        """ Test for checking id with special char """
        id_key_special_char = "é123456789"
        id_number_special_char = "J1234567+9"
        self.assertEqual(is_id_valid(id_key_special_char), False)
        self.assertEqual(is_id_valid(id_number_special_char), False)

    def test_id_not_a_string(self):
        """ Test for checking id with bad var type """
        id_integer = 1745896325
        id_dictionary = {"id": "J123456789"}
        id_list = ["J123456789"]
        id_bool = True
        id_null = None
        self.assertEqual(is_id_valid(id_integer), False)
        self.assertEqual(is_id_valid(id_dictionary), False)
        self.assertEqual(is_id_valid(id_list), False)
        self.assertEqual(is_id_valid(id_bool), False)
        self.assertEqual(is_id_valid(id_null), False)


# Tests for function 'check_id'
class TestIDChecker(BaseTestCase):
    good_response = {
        'status': 'successfully finished',
        'request': None,
        'result': None
    }

    bad_response = {
        'status': 'successfully finished - but input not valid format (1 maj letter and 9 numbers expected)',
        'request': None,
        'result': None
    }

    def test_good_id(self):
        """ Test for checking good id """
        response = self.good_response
        good_id1 = "J123456789"
        good_id2 = "Z009999999"
        response["result"] = 1
        response["request"] = good_id1
        self.assertEqual(check_id(good_id1), response)
        response["request"] = good_id2
        self.assertEqual(check_id(good_id2), response)

    def test_bad_id(self):
        """ Test for checking bad id - numbers not corresponding to letter """
        response = self.bad_response
        bad_id1 = "A123456789"
        bad_id2 = "Z029999999"
        response["result"] = 0
        response["request"] = bad_id1
        self.assertEqual(check_id(bad_id1), response)
        response["request"] = bad_id2
        self.assertEqual(check_id(bad_id2), response)


# Tests for function 'alpha_corresponds_to_total'
class TestAlphaCorrespondsTotal(BaseTestCase):
    def test_alpha_corresponds(self):
        """ Test for checking alpha who corresponds to total """
        self.assertEqual(alpha_corresponds_to_total("Z", 0), True)
        self.assertEqual(alpha_corresponds_to_total("B", 2), True)
        self.assertEqual(alpha_corresponds_to_total("J", 10), True)

    def test_alpha_dont_corresponds(self):
        """ Test for checking alpha who dont corresponds to total """
        self.assertEqual(alpha_corresponds_to_total("Z", 4), False)
        self.assertEqual(alpha_corresponds_to_total("B", 9), False)
        self.assertEqual(alpha_corresponds_to_total("J", 0), False)


if __name__ == '__main__':
    unittest.main()
