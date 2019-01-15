import unittest
from suburbs import *

class TestSuburbs(unittest.TestCase):

    def test_make_new_suburb(self):
        self.assertIsNotNone(city_suburbs, msg=None)

if __name__ == '__main__':
    unittest.main()