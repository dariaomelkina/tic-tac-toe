# required: pip install termcolor
from board import Board
from termcolor import cprint


def main():
    """
    () -> str
    Simulate tic-tack-toe game.
    """
    board = Board()
    while True:
        board.person_move()
        state = board.state()
        if state:
            return state
        board.computer_move()
        state = board.state()
        if state:
            return state


if __name__ == '__main__':
    cprint('Welcome to the Tic-Tac-Toe game!', 'magenta')
    end = main()
    if end == 'X':
        cprint('Congratulations! You won that game!', 'cyan')
    elif end == 'O':
        cprint('That time computer won.', 'yellow')
    else:
        cprint('Draw! No has won, no one has lost.', 'magenta')
