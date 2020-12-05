import unittest

from app.test.base import BaseTestCase
from app.main.service.client_service import checkID

class TestIDCheckerCase(BaseTestCase):

    def test_good_id(self):
            """ Test for checking good id """
            good_id1 = "J123456789"
            good_id2 = "Z009999999"
            response = checkID(good_id1)
            self.assertEqual(response, True)
            response = checkID(good_id2)
            self.assertEqual(response, True)
    
    def test_bad_id(self):
            """ Test for checking bad id """
            bad_id1 = "A123456789"
            bad_id2 = "Z023456789"
            response = checkID(bad_id1)
            self.assertEqual(response, False)
            response = checkID(bad_id2)
            self.assertEqual(response, False)
    
    def test_id_bad_length(self):
            """ Test for checking bad length id """
            bad_id1 = "A1234567890"
            bad_id2 = "Z02345678"
            response = checkID(bad_id1)
            self.assertEqual(response, False)
            response = checkID(bad_id2)
            self.assertEqual(response, False)
    
    def test_id_key_not_letter(self):
            """ Test for checking id with no letter """
            bad_id = "01234567890"
            response = checkID(bad_id)
            self.assertEqual(response, False)


if __name__ == '__main__':
    unittest.main()