import unittest

from parsers.armor import parse, parse_secondary


class TestArmorParser(unittest.TestCase):
    def test_standard(self):
        line = 'Lightweight Poly Carapace +12 11 - 2 Cr15000 None'
        expected = [
            'Lightweight Poly Carapace',
            '12',
            '',
            '',
            '11',
            '-',
            '2',
            'Cr15000',
            'None'
        ]
        tokens = parse(line)
        self.assertEqual(expected, tokens)

    def test_alternate(self):
        line = 'Ablat +1 (+6 vs. lasers) 9 - 2 Cr75 None'
        expected = [
            'Ablat',
            '1',
            '6',
            'lasers',
            '9',
            '-',
            '2',
            'Cr75',
            'None'
        ]
        tokens = parse(line)
        self.assertEqual(expected, tokens)

    def test_psi(self):
        line = 'Psi-Enhanced Combat Armour +15 (+ ½ PSI) 16 250 10 Cr500000 None'
        expected = [
            'Psi-Enhanced Combat Armour',
            '15',
            '½',
            'PSI',
            '16',
            '250',
            '10',
            'Cr500000',
            'None'
        ]
        tokens = parse(line)
        self.assertEqual(expected, tokens)

    def test_secondary(self):
        line = '+6 vs. lasers'
        expected = (
            '6',
            'lasers',
        )
        tokens = parse_secondary(line)
        self.assertEqual(expected, tokens)


if __name__ == '__main__':
    unittest.main()