from collections import Counter
from enum import Enum
import numpy.random


class Move(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

WIN_DICT = {
    Move.ROCK: Move.SCISSORS,
    Move.PAPER: Move.ROCK,
    Move.SCISSORS: Move.PAPER,
}

class HistoricalMoveStrategy:
    def __init__(self):
        self.memory_log = []
    
    def log_move(self, player_move):
        self.memory_log.append(player_move)

    def get_strategy(self):
        mem = Counter(self.memory_log)
        p = [mem[WIN_DICT[move]] for move in Move]
        try:
            return [x/sum(p) for x in p]
        except:
            pass


def get_player_move():
    while True:
        instruction = ', '.join([f'{move.name}: {move.value}' for move in Move])
        instruction += ' (input "q" to quit)'
        print(instruction)
        player_input = input('Please enter your move: ')
        try:
            if player_input == 'q':
                break
            return Move(int(player_input))
        except:
            print('Wrong input, please enter again.')


def get_computer_move(strategy=None):
    return Move(numpy.random.choice([move.value for move in Move], p=strategy))


def check_winner(player_move, computer_move):
    if player_move == computer_move:
        return 'tie'
    elif computer_move == WIN_DICT[player_move]:
        return 'win'
    else:
        return 'lose'


if __name__ == '__main__':
    # initiate strategy to record player's move
    hist_strategy = HistoricalMoveStrategy()

    while True:
        p_move = get_player_move()
        hist_strategy.log_move(p_move)
        if p_move is None:  # exit by breaking from while-loop
            break

        c_move = get_computer_move(strategy=hist_strategy.get_strategy())
        result = check_winner(p_move, c_move)

        # printing result message
        if result == 'tie':
            print(f"Both selected {p_move}, it's a TIE")
        elif result == 'win':
            print(f'Computer displays {Move(c_move).name}, you WIN!')
        elif result == 'lose':
            print(f'Computer displays {Move(c_move).name}, you LOSE!')

    print('\nSee you next time!')