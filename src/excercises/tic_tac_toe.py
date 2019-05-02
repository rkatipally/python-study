import itertools


class TicTacToe:
    @staticmethod
    def draw_board(cells):
        print('\n'*100)
        rows = '\n' + '-'*13 + '\n'
        for row in range(3):
            for col in range(13):
                rem = col%4
                quotient = col//4
                if rem == 2:
                    rows = rows + str( cells[3*row + quotient])
                elif rem == 0:
                    rows = rows + '|'
                else:
                    rows = rows + ' '
            rows = rows + '\n' + '-'*13 + '\n'
        print(rows)

    @staticmethod
    def is_game_won(choices):
        for player, positions in choices.items():
            for comb in itertools.combinations(positions, 3):
                if comb[0] - comb[1] == comb[1] - comb[2]:
                    return True
        return False

    @staticmethod
    def is_valid_choice(choices, cells, selected):
        if not (1 <= selected < len(cells)):
            return False
        for player, positions in choices.items():
            for filled_cell in positions:
                if filled_cell == selected:
                    return False
        return True

    def start_game(self):
        cells = list(range(1,10))
        players = ['A', 'B']
        choices  = {'A': [], 'B': []}
        is_first = True
        self.draw_board(cells)
        player = players[0]
        i = 0
        while i < len(cells):
            print('Player {0}:'.format(player))
            chosen_cell = int(input())
            if not self.is_valid_choice(choices, cells, chosen_cell):
                print('Please select a valid choice!')
                continue
            else:
                i += 1
                cells[chosen_cell-1] = player
                choices.get(player).append(chosen_cell)
                if self.is_game_won(choices):
                    print('Player {0} wins the game!'.format(player))
                    break
                else:
                    player = players[int(is_first)]
                    is_first = not is_first
                self.draw_board(cells)


tic_tac_toe = TicTacToe()
tic_tac_toe.start_game()





