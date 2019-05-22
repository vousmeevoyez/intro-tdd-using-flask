import unittest

from app.modules.converter import Converter

class TestConverter(unittest.TestCase):

    def test_gram_to_idr(self):
        # build simple test to just pass the test
        result = Converter("buy").gram_to_idr(1)
        # go back to Converter file and write more code!

        # now lets test out the code has been written
        result = Converter("buy").gram_to_idr(1)
        # check the result and make sure the result is correct!
        self.assertEqual(result, 627000)

        # now lets test out the code has been written
        result = Converter("sell").gram_to_idr(1)
        # check the result and make sure the result is correct!
        self.assertEqual(result, 598880)

    def test_gram_to_idr_cant_be_zero(self):
        with self.assertRaises(ValueError):
            result = Converter("buy").gram_to_idr(0)
