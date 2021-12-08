'''
Tests for the translator module
Author: Jubran Akram
'''

import unittest
from translator import french_to_english, english_to_french


class TestEnglish2French(unittest.TestCase):
    '''Tests english_to_french function'''

    def test_null_input(self):
        '''Tests when no input is provided'''
        self.assertIsNone(english_to_french(None))

    def test_hello(self):
        '''Tests the translation of the English word = Hello'''
        self.assertEqual(english_to_french('Hello').get(
            'translations')[0].get('translation'), 'Bonjour')

    def test_howareyou(self):
        '''Tests the translation of the English phrase = How are you?'''
        self.assertNotEqual(english_to_french('How are you?').get(
            'translations')[0].get('translation'), 'Comment')


class TestFrench2English(unittest.TestCase):
    '''Tests french_to_english function'''

    def test_null_input(self):
        '''Tests when no input is provided'''
        self.assertIsNone(french_to_english(None))

    def test_hello(self):
        '''Tests the translation of the French word = Bonjour'''
        self.assertEqual(french_to_english('Bonjour').get(
            'translations')[0].get('translation'), 'Hello')

    def test_howareyou(self):
        '''Tests the translation of the French phrase = Comment es-tu?'''
        self.assertEqual(french_to_english(
            'Comment es-tu?').get('translations')[0].get('translation'), 'How are you?')


if __name__ == '__main__':
    unittest.main()
