from src.excercises.black_jack.black_jack_main import BlackJack
from unittest import TestCase


class BlackJackTester(TestCase):

    def test_generate_cards(self):
        black_jack = BlackJack('Raj', 1000)
        black_jack.generate_cards()
        self.assertEqual(52, len(black_jack.deck))
        self.assertEqual(4, black_jack.deck.count('A'))
        self.assertEqual(4, black_jack.deck.count(2))
        self.assertEqual(4, black_jack.deck.count(3))
        self.assertEqual(4, black_jack.deck.count(4))
        self.assertEqual(4, black_jack.deck.count(5))
        self.assertEqual(4, black_jack.deck.count(6))
        self.assertEqual(4, black_jack.deck.count(7))
        self.assertEqual(4, black_jack.deck.count(8))
        self.assertEqual(4, black_jack.deck.count(9))
        self.assertEqual(4, black_jack.deck.count(10))
        self.assertEqual(4, black_jack.deck.count('J'))
        self.assertEqual(4, black_jack.deck.count('Q'))
        self.assertEqual(4, black_jack.deck.count('K'))
