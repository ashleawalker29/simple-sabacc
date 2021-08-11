import unittest

from card import Card


class CardTests(unittest.TestCase):

    def test_defaulted_card(self):
        test_cards = [Card(None, None), Card('test', None), Card(None, 'Circles'),
                      Card(5, 'Test Stave'), Card(0, 'Sylop'), Card(5, 'Sylop'),
                      Card(0, 'Triangles')]

        for test_card in test_cards:
            self.assertEqual(test_card.value, 0)
            self.assertEqual(test_card.stave, 'Sylop')

    def test_value_is_int(self):
        test_cards = [Card(None, None), Card('test', None), Card(None, 'Circles'),
                      Card(5, 'Test Stave'), Card(0, 'Sylop'), Card(5, 'Sylop'),
                      Card(0, 'Triangles'), Card(5, 'Circles')]

        for test_card in test_cards:
            self.assertTrue(type(test_card.value) is int)

    def test_value_between_0_and_10(self):
        test_cards = [Card(None, None), Card('test', None), Card(None, 'Circles'),
                      Card(5, 'Test Stave'), Card(0, 'Sylop'), Card(5, 'Sylop'),
                      Card(0, 'Triangles'), Card(5, 'Circles')]

        for test_card in test_cards:
            self.assertTrue(0 <= test_card.value <= 10)

    def test_is_staves_valid(self):
        # Test cards that should default to Card(0, 'Sylop')
        test_cards = [Card(None, None), Card('test', None), Card(None, 'Circles'),
                      Card(5, 'Test Stave'), Card(0, 'Sylop'), Card(5, 'Sylop'),
                      Card(0, 'Triangles')]

        for test_card in test_cards:
            self.assertTrue(test_card.stave, 'Sylop')

        # Test cards that should be considered valid.
        test_cards = [Card(5, 'Circles'), Card(5, 'Triangles'), Card(5, 'Squares'),
                      Card(0, 'Sylop')]

        for test_card in test_cards:
            self.assertTrue(test_card.stave in ['Circles', 'Triangles', 'Squares', 'Sylop'])


if __name__ == '__main__':
    unittest.main()
