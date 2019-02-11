def function():
    passimport unittest
# from city import *
from suburbs import *

""" #FIXME
class TestCity(unittest.TestCase):
    
    # TODO: make city test work
    @patch('city.input', return_value='2000')
    def test_market_suburb(self, input):
        # input will return '2000' during this test
        self.assertIsNotNone(city_suburbs[-1].size, msg=None)
"""

class TestSuburbs(unittest.TestCase):

    def test_make_new_suburb(self):
        self.assertIsNotNone(city_suburbs, msg=None)

if __name__ == '__main__':
    unittest.main()