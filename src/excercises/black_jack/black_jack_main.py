import random
from enum import Enum
from functools import reduce


class Player(Enum):
    NAME = 'name'
    BALANCE = 'balance'
    CURRENT_BET = 'current_bet'
    HAND = 'hand'


class Dealer(Enum):
    HAND = 'hand'


class BlackJack:
    cards = []
    cards_suit = {'A': 10, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10}
    player = {Player.NAME: '', Player.BALANCE: 0, Player.CURRENT_BET: 0, Player.HAND: []}
    dealer = {Dealer.HAND: []}

    def __init__(self, player_name, player_balance):
        print('Black Jack Game'.center(100, '='))
        self.player[Player.NAME] = player_name
        self.player[Player.BALANCE] = player_balance

    def start_game(self):
        self.generate_cards()
        self.ask_for_bet()
        self.deal_cards()
        self.continue_game()
        self.show_balance()

    def continue_game(self):
        is_stand = False
        while True:
            self.show_hands(is_stand)
            if self.is_black_jack(self.player[Player.HAND]):
                print('OHHOOOO its a BlackJack, you win!!')
                break

            if self.is_black_jack(self.dealer[Dealer.HAND]):
                print('BlackJack for dealer, you lose!!')
                break

            if self.is_bust() or (is_stand and self.dealer_wins()):
                print('Dealer Wins!!')
                self.player[Player.BALANCE] = self.player[Player.BALANCE] - self.player[Player.CURRENT_BET]
                break
            elif not is_stand:
                print('Hit or Stand [h/s]?:')
                choice = input()
                if choice.lower() == 'h':
                    self.deal_cards(True, False)
                else:
                    is_stand = True
                continue
            else:
                if self.continue_for_dealer():
                    self.deal_cards(False, True)
                else:
                    print('You Win!!!')
                    self.player[Player.BALANCE] = self.player[Player.BALANCE] + self.player[Player.CURRENT_BET]
                    break

    def dealer_wins(self):
        return (not self.continue_for_dealer()) and (
                self.hand_total(self.dealer[Dealer.HAND]) > self.hand_total(self.player[Player.HAND]))

    def continue_for_dealer(self):
        return self.hand_total(self.dealer[Dealer.HAND]) < 17

    def is_bust(self):
        return self.hand_total(self.player[Player.HAND]) > 21

    def is_black_jack(self, hand):
        return self.hand_total(hand) == 21

    def hand_total(self, hand):
        return reduce(lambda a, b: a + b, map(lambda x: self.cards_suit.get(x), hand))

    def deal_cards(self, is_player=False, is_dealer=False):
        if is_player:
            self.player[Player.HAND].append(self.cards.pop())
        elif is_dealer:
            self.dealer[Dealer.HAND].append(self.cards.pop())
        else:
            self.player[Player.HAND].append(self.cards.pop())
            self.dealer[Dealer.HAND].append(self.cards.pop())
            self.player[Player.HAND].append(self.cards.pop())
            self.dealer[Dealer.HAND].append(self.cards.pop())

    def ask_for_bet(self):
        while True:
            try:
                print(f'{self.player[Player.NAME]}, Your current balance is {self.player[Player.BALANCE]}')
                print('Place your bet!!')
                bet_amount = int(input())
                if bet_amount < self.player[Player.BALANCE]:
                    self.player[Player.CURRENT_BET] = bet_amount
                else:
                    print(f'Naughty!!! Not enough chips!!!')
            except ValueError:
                print('Invalid amount!!')
                continue
            else:
                print(f'Lets see if you can win, {self.player[Player.NAME]}')
                break

    def generate_cards(self):
        for i in range(4):
            for key in self.cards_suit.keys():
                self.cards.append(key)
        # shuffle the cards
        random.shuffle(self.cards)

    def show_hands(self, is_stand):
        if is_stand:
            print("Your Hand:: {0}\nDealer's Hand:: {1}".format(self.player[Player.HAND], self.dealer[Dealer.HAND]))
        else:
            mask_hand = [self.dealer[Dealer.HAND][0], '*']
            print("Your Hand:: {0}\nDealer's Hand:: {1}".format(self.player[Player.HAND], mask_hand))

    def show_balance(self):
        print(f'Your current balance is {self.player[Player.BALANCE]}')

    def __str__(self):
        return '''Player::{0}, Current Balance::{1}, Current Bet::{2}, Hand::{3}\nDealer's Hand:: {4}'''.format(
            self.player[Player.NAME],
            self.player[Player.BALANCE],
            self.player[
                Player.CURRENT_BET],
            self.player[Player.HAND],
            self.dealer[Dealer.HAND])


if __name__ == '__main__':
    black_jack = BlackJack('Raj', 1000)
    black_jack.start_game()
