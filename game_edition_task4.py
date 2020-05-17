# required: pip install termcolor
from board import Board
from termcolor import cprint
from tree_task_4 import Tree
import copy

class BoardSecondEdition(Board):
    def __init__(self):
        super().__init__()
        self.tree = None
        self._last_symbol = None

    def tree(self):
        tree = Tree(self)
        def recursion(board, tree):
            possible = self.possible()
            if len([i for i in possible.keys()]) < 2:
                board1 = copy.deepcopy(board)
                if self._last_symbol == 'X':
                    board1.add_pos(possible[1][0], possible[1][1], 'O')
                else:
                    board1.add_pos(possible[1][0], possible[1][1], 'X')
                tree.add_child(board1)
            else:
                if self._last_symbol == "O":
                    symbol = "X"
                else:
                    symbol = "O"
                for i in possible.keys():
                    board1 = copy.deepcopy(board)
                    board1.add_pos(possible[i][0], possible[i][1], symbol)
                    tree.add_child(board1)
                for i in tree.children:
                    recursion(i.key, i)
        recursion(self, tree)
        self.tree = tree

    def computer_move(self):
        lst = self.tree.childen
        points = []
        for i in lst

    def cut_tree(self):
        for i in self.tree.children:
            if i.key == self:
                self.tree = i

    def __eq__(self, other):
        if self.positions == other.positions:
            return True
        return False


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
        cprint('Draw! No one has won, no one has lost.', 'magenta')
