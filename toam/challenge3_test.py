import unittest
from challenge3 import incr_dict

class DictTestCase(unittest.TestCase):
    '''Tests for incr_dict'''
    def test_one_element_tuple_with_empty_dict(self):
        '''should return {'a':1}'''
        self.assertEqual(incr_dict({}, ('a')), {'a':1})

    def test_multiple_element_tuple_with_empty_dict(self):
        '''should return {'a':{'b'{'c':1}}}'''
        self.assertEqual(incr_dict({}, ('a', 'b', 'c')), {'a':{'b':{'c':1}}})

if __name__ == '__main__':
    unittest.main()
