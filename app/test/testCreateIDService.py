"""testCreateIDService.py: All the unit test for create_id_service functions."""
__author__      = "Girard Alexandre"

import unittest

from app.test.base import BaseTestCase

# Import all functions to be tested
from app.main.service.create_id_service import createID, createCompleteID, inputIsValid, getLetterByTotal

# Tests for function 'inputIsValid'
class TestInputValidator(BaseTestCase):
    def test_good_input(self):
        """ Test for checking good inputs """
        good_input1 = "123456789"
        good_input2 = "009999999"
        self.assertEqual(inputIsValid(good_input1), True)
        self.assertEqual(inputIsValid(good_input2), True)
    
    def test_inputs_bad_length(self):
        """ Test for checking bad length inputs """
        input_too_long = "1234567890"
        input_too_short = "02345678"
        input_empty = ""
        self.assertEqual(inputIsValid(input_too_long), False)
        self.assertEqual(inputIsValid(input_too_short), False)
        self.assertEqual(inputIsValid(input_empty), False)
    
    def test_input_with_other_char_than_numbers(self):
        """ Test for checking input with bad chars """
        input_with_letter = "12A456789"
        input_with_special_char = "1234567+9"
        self.assertEqual(inputIsValid(input_with_letter), False)
        self.assertEqual(inputIsValid(input_with_special_char), False)

    def test_input_not_a_string(self):
        """ Test for checking input with bad var type """
        id_integer = 174589632
        id_dictionary = { "id": "123456789" }
        id_list = ["123456789"]
        id_bool = True
        id_null = None
        self.assertEqual(inputIsValid(id_integer), False)
        self.assertEqual(inputIsValid(id_dictionary), False)
        self.assertEqual(inputIsValid(id_list), False)
        self.assertEqual(inputIsValid(id_bool), False)
        self.assertEqual(inputIsValid(id_null), False)


# Tests for function 'createCompleteID' -- it can only have good inputs (verified before)
class TestCompleteIDCreator(BaseTestCase):
    def test_good_input(self):
        """ Test for checking good inputs """
        input1 = "123456789"
        input2 = "009999999"
        self.assertEqual(createCompleteID(input1), "J123456789")
        self.assertEqual(createCompleteID(input2), "Z009999999")


# Tests for function 'getLetterByTotal'
class TestGetLetterByTotal(BaseTestCase):
    def test_some_totals(self):
        """ Test with some totals """
        total1 = 0
        total2 = 4
        total3 = 8
        self.assertEqual(getLetterByTotal(total1), "Z")
        self.assertEqual(getLetterByTotal(total2), "D")
        self.assertEqual(getLetterByTotal(total3), "H")


# Tests for function 'createID'
class TestIDCreator(BaseTestCase):
    good_response = {
        'status': 'successfully finished',
        'request': None,
        'result': None
    }
    
    bad_response = {
        'status': 'successfully finished - but input not valid format (9 numbers expected)',
        'request': None,
        'result': None
    }
    
    def test_good_input(self):
        """ Test for creating with good input """
        response = self.good_response
        good_input1 = "123456789"
        good_input2 = "009999999"
        response["request"] = good_input1
        response["result"] = "J123456789"
        self.assertEqual(createID(good_input1), response)
        response["request"] = good_input2
        response["result"] = "Z009999999"
        self.assertEqual(createID(good_input2), response)
    
    def test_bad_input(self):
        """ Test for checking bad input - not good format """
        response = self.bad_response
        bad_input1 = "23456789"
        bad_input2 = "A02999999"
        response["result"] = "null"
        response["request"] = bad_input1
        self.assertEqual(createID(bad_input1), response)
        response["request"] = bad_input2
        self.assertEqual(createID(bad_input2), response)