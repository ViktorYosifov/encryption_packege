import unittest


from encrypt_sp.helper.rot_13 import *

class TestRot13(unittest.TestCase):

    def test_rot13_fixed_strings(self):
        self.assertEqual(rot_13('test'), 'grfg')
        self.assertEqual(rot_13('Test'), 'Grfg')
        self.assertEqual(rot_13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%')

    def test_rot13_decrypt(self):
        self.assertEqual(rot_13('grfg'), 'test')
        self.assertEqual(rot_13('Grfg'), 'Test')
        self.assertEqual(rot_13('nN oO mM 1234 *!?%'), 'aA bB zZ 1234 *!?%')