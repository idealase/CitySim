import unittest
from city import *

class TestCity(unittest.TestCase):
    
    # TODO: make city test work
    @patch('city.input', return_value='2000')
    def test_market_suburb(self, input):
        # input will return '2000' during this test
        self.assertIsNotNone(city_suburbs[-1].size, msg=None)