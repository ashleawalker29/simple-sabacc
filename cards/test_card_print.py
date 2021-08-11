import unittest

from unittest.mock import patch
from card import Card

class CardTests(unittest.TestCase):

    @patch('builtins.print')
    def test_card_print_sylop(self, mock_print):
        test_card = Card(0, 'Sylop')
        test_card.print()

        mock_print.assert_called_with('Sylop')

    @patch('builtins.print')
    def test_card_print_circles(self, mock_print):
        test_card = Card(5, 'Circles')
        test_card.print()

        mock_print.assert_called_with('5 of Circles')

    @patch('builtins.print')
    def test_card_print_triangles(self, mock_print):
        test_card = Card(5, 'Triangles')
        test_card.print()

        mock_print.assert_called_with('5 of Triangles')

    @patch('builtins.print')
    def test_card_print_squares(self, mock_print):
        test_card = Card(5, 'Squares')
        test_card.print()

        mock_print.assert_called_with('5 of Squares')

if __name__ == '__main__':
    unittest.main()
