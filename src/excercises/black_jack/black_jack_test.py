from src.excercises.black_jack.black_jack_main import BlackJack
from unittest import TestCase


class BlackJackTester(TestCase):

    def test_generate_cards(self):
        black_jack = BlackJack('Raj', 1000)
        black_jack.generate_cards()
        self.assertEqual(52, len(black_jack.cards))
        self.assertEqual(4, black_jack.cards.count('A'))
        self.assertEqual(4, black_jack.cards.count(2))
        self.assertEqual(4, black_jack.cards.count(3))
        self.assertEqual(4, black_jack.cards.count(4))
        self.assertEqual(4, black_jack.cards.count(5))
        self.assertEqual(4, black_jack.cards.count(6))
        self.assertEqual(4, black_jack.cards.count(7))
        self.assertEqual(4, black_jack.cards.count(8))
        self.assertEqual(4, black_jack.cards.count(9))
        self.assertEqual(4, black_jack.cards.count(10))
        self.assertEqual(4, black_jack.cards.count('J'))
        self.assertEqual(4, black_jack.cards.count('Q'))
        self.assertEqual(4, black_jack.cards.count('K'))
