import unittest

from parsers.battledress import parse


class TestArmorParser(unittest.TestCase):
    def test_standard(self):
        line = 'Artillery Battle Dress +26 13 245 +6 +2 30 180 Cr275000 Vacc Suit 2'
        expected = [
            'Artillery Battle Dress',
            '26',
            '',
            '',
            '13',
            '245',
            '+6',
            '+2',
            '30',
            '180',
            'Cr275000',
            'Vacc Suit 2'
        ]
        tokens = parse(line)
        self.assertEqual(expected, tokens)


if __name__ == '__main__':
    unittest.main()