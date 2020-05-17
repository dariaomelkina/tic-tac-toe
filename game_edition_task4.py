# required: pip install termcolor
from board import Board
from termcolor import cprint
from tree_task_4 import Tree

class BoardSecondEdition(Board):
    def __init__(self):
        super().__init__()
        self.tree = None

    def tree(self):

    def computer_move(self):


def main():
    board = Board()
    board.person_move()
    board.tree()
    while True:
        board.computer_move()
        state = board.state()
        if state:
            return state
        board.cut_tree()
        board.person_move()
        state = board.state()
        if state:
            return state
        board.cut_tree()

if __name__ == '__main__':
    cprint('Welcome to the Tic-Tac-Toe game: Second edition!', 'magenta')
    end = main()
    if end == 'X':
        cprint('Congratulations! You won that game!', 'cyan')
    elif end == 'O':
        cprint('That time computer won.', 'yellow')
    else:
        cprint('Draw! No has won, no one has lost.', 'magenta')
