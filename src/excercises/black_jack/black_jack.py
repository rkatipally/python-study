import random
from functools import reduce


class BlackJack:

    def __init__(self):
        self.deck = Deck()
        self.playing = True
        self.dealer = Dealer()
        self.player = Player('Raj', 1000)
        self.start_game()

    def start_game(self):
        self.take_bet()
        self.deal_cards(False, False)
        if self.player_blackjack():
            print('BlakcJack !!!')
            self.player.win_bet()
        else:
            self.hit_or_stand()
            while True:
                if self.playing:
                    self.hit()
                    if self.player_busts():
                        print('Game Over, you lose!!')
                        self.player.lose_bet()
                        break
                    elif self.player_blackjack():
                        print('BlakcJack !!!')
                        self.player.win_bet()
                    else:
                        self.hit_or_stand()
                        continue
                else:
                    if not (self.dealer_busts() or self.deal_wins() or self.push()):
                        self.deal_cards(False, True)
                        if self.push():
                            print('Its a push')
                            break
                        if self.deal_wins():
                            print("Dealer Wins")
                            self.player.lose_bet()
                            break
                        if self.dealer_busts():
                            print("You Win")
                            self.player.win_bet()
                            break
                        if self.dealer_blackjack():
                            print('Dealer BlackJack!!!')
                            self.player.lose_bet()
                            break

    def player_blackjack(self):
        return self.player.hand.value == 21

    def dealer_blackjack(self):
        return self.dealer.hand.value == 21

    def player_busts(self):
        return self.player.hand.value > 21

    def player_win(self):
        return (not self.player_busts() and (
                self.player.hand.value > self.dealer.hand.value) and self.dealer.hand.value >= 17) or self.dealer_busts()

    def dealer_busts(self):
        return self.dealer.hand.value > 21

    def deal_wins(self):
        return (not self.dealer_busts() and (
                self.dealer.hand.value > self.player.hand.value) and self.dealer.hand.value >= 17) or self.player_busts()

    def push(self):
        return (self.dealer.hand.value >= 17 and self.dealer.hand.value) == self.player.hand.value

    def hit(self):
        self.deal_cards(True, False)

    def hit_or_stand(self):
        print('Hit or Stand [h/s]?:')
        choice = input()
        if choice.lower() == 'h':
            self.playing = True
        else:
            self.playing = False

    def deal_cards(self, is_player=False, is_dealer=False):
        if is_player:
            self.player.add_card(self.deck.deal_card())
        elif is_dealer:
            self.dealer.add_card(self.deck.deal_card())
        else:
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())
            self.player.add_card(self.deck.deal_card())
            self.dealer.add_card(self.deck.deal_card())
        self.show_cards(is_dealer)

    def show_cards(self, is_stand=False):
        if is_stand:
            print(f"Dealer's Hand: [{str(self.dealer.hand)}], Your Hand: [{str(self.player.hand)}]")
        else:
            print(f"Dealer's Hand: [{str(self.dealer.hand.cards[0])}, *] , Your Hand: [{str(self.player.hand)}]")

    def ask_name_and_chips(self):
        print('Please enter your name')
        name = int(input())
        while True:
            try:
                print('Please enter your chips')
                chips_total = int(input())
            except ValueError:
                print('Please enter valid amount')
                continue
            else:
                self.player = Player(name, chips_total)
                break

    def take_bet(self):
        while True:
            try:
                print('Please enter your bet')
                bet = int(input())
                if bet > self.player.chips.total:
                    print('Please enter below your limit - ' + self.player.chips.total)
                    continue
                self.player.add_bet(bet)
            except ValueError:
                print('Please enter valid amount')
                continue
            else:
                break


class Dealer:
    def __init__(self):
        self.hand = Hand()

    def add_card(self, card):
        self.hand.add_card(card)

    def adjust_for_ace(self):
        self.adjust_for_ace()

    def get_hand(self):
        return self.hand


class Player:
    def __init__(self, name, chips_total):
        self.name = name
        self.chips = Chips(chips_total)
        self.hand = Hand()

    def add_bet(self, bet):
        self.chips.add_bet(bet)

    def win_bet(self):
        self.chips.win_bet()

    def lose_bet(self):
        self.chips.lose_bet()

    def add_card(self, card):
        self.hand.add_card(card)

    def adjust_for_ace(self):
        self.hand.adjust_for_ace()

    def get_hand(self):
        return self.hand

    def __str__(self):
        return f'Name: {self.name}, chips: {self.chips.total}, current bet: {self.chips.bet}'


class Chips:

    def __init__(self, total):
        self.total = total
        self.bet = 0

    def add_bet(self, bet):
        self.bet = bet

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value

    def adjust_for_ace(self):
        for card in self.cards:
            if card.rank == 'Ace':
                card.value = 1

    def __str__(self):
        return f'Cards: {reduce(lambda x, y: ",".join([str(x), str(y)]), self.cards)}, Value: {self.value}'


class Card:

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10,
              'Queen': 10, 'King': 10, 'Ace': 11}

    cards = []

    def __init__(self):
        self.create_deck()
        self.shuffle_cards()

    def create_deck(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank, self.values.get(rank)))

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

    def __str__(self):
        deck_str = ''
        for card in self.cards:
            deck_str += str(card) + ', '
        return deck_str


if __name__ == '__main__':
    black_jack = BlackJack()
