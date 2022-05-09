import unittest

from baseencoder import BaseEncoder


class BaseEncoderTestCase(unittest.TestCase):
    def setUp(self):
        self.enc = BaseEncoder()

    def test_encoding_and_decoding(self):
        # No matter the encoding, decoding an encoded string should
        # return the original string
        for word in ['TEST', 'HELLO', 'REDI']:
            self.assertEqual(self.enc.decode(self.enc.encode(word)), word)