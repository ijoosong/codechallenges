import unittest
from challenge3 import incr_dict

class DictTestCase(unittest.TestCase):
    '''Tests for incr_dict'''
    def test_one_element_tuple_with_empty_dict(self):
        '''should return {'a':1}'''
        tup = ('a')
        self.assertEqual(incr_dict({}, tup), {'a':1})

    def test_multiple_element_tuple_with_empty_dict(self):
        '''should return {'a':{'b'{'c':1}}}'''
        tup = ('a', 'b', 'c')
        self.assertEqual(incr_dict({}, tup), {'a':{'b':{'c':1}}})

    def test_one_element_tuple_with_prexisting_dict(self):
        '''should return {'a':{'b':{'c':1}}, 'd':1}'''
        dct = {'a':{'b':{'c':1}}}
        tup = ('d')
        self.assertEqual(incr_dict(dct, tup), {'a':{'b':{'c':1}}, 'd':1})

    def test_multiple_element_tuple_that_completely_overlaps_with_prexisting_dict(self):
        '''should return {'a':{'b':{'c':2}}}'''
        dct = {'a':{'b':{'c':1}}}
        tup = ('a', 'b', 'c')
        self.assertEqual(incr_dict(dct, tup), {'a':{'b':{'c':2}}})

    def test_multiple_element_tuple_that_partially_overlaps_with_prexisting_dict(self):
        '''should return {'a':{'b':{'c':1, 'd':1}}}'''
        dct = {'a':{'b':{'c':1}}}
        tup = ('a', 'b', 'd')
        self.assertEqual(incr_dict(dct, tup), {'a':{'b':{'c':1, 'd':1}}})

    def test_multiple_element_tuple_that_has_no_overlaps_with_prexisting_dict(self):
        '''should return {'a':{'b':{'c':1}}, 'x':{'y':{'z':1
        }}}'''
        dct = {'a':{'b':{'c':1}}}
        tup = ('x','y','z')
        self.assertEqual(incr_dict(dct, tup), {'a':{'b':{'c':1}},'x':{'y':{'z':1}}})

    def test_one_element_tuple_with_prexisting_dict(self):
        '''should return {'a':{'b':{'c':1}}, 'd':1}'''
        dct = {'a':{'b':{'c':1}}}
        tup = ('d')
        self.assertEqual(incr_dict(dct, tup), {'a':{'b':{'c':1}}, 'd':1})

    def test_tuples_that_arent_strings(self):
        dct = {}
        tup = (1, 2, 3)
        self.assertEqual(incr_dict(dct, tup), {1:{2:{3:1}}})
if __name__ == '__main__':
    unittest.main()
