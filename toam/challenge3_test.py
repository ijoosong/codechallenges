import unittest
from challenge3 import incr_dict

class DictTestCase(unittest.TestCase):
    '''Tests for incr_dict'''
    def test_one_element_tuple_with_empty_dict(self):
        '''should return {'a':1}'''
        tup = ('a')
        self.assertEqual(incr_dict({}, tup, {'a':1})

    def test_multiple_element_tuple_with_empty_dict(self):
        '''should return {'a':{'b'{'c':1}}}'''
        tup = ('a', 'b', 'c')
        self.assertEqual(incr_dict({}, tup, {'a':{'b':{'c':1}}})

    def test_one_element_tuple_with_prexisting_dict(self):
        '''should return {'a':{'b':{'c':1}}, 'd':1}'''
        dct = {'a':{'b':{'c':1}}}
        tup = ('d')
        self.assertEqual(incr_dict(dct, tup), {'a':{'b':{'c':1}}, 'd':1})

    def test_multiple_element_tuple_with_prexisting_dict(self):
        
if __name__ == '__main__':
    unittest.main()
