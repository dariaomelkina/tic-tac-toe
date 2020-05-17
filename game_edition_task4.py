# required: pip install termcolor
from board import Board
from termcolor import cprint
from tree_task_4 import Tree
import copy


class BoardSecondEdition(Board):
    """ Class for board representation (second edition). """

    def __init__(self):
        """
        (BoardSecondEdition) -> NoneType
        Create new board.
        """
        super().__init__()
        self.tree = None

    def make_tree(self):
        """
        (BoardSecondEdition) -> NoneType
        Build a tree for the game possibilities.
        """
        tree = Tree(self)

        def recursion(board, tree):
            possible = board.possible()
            if len([i for i in possible.keys()]) < 2:
                board1 = copy.deepcopy(board)
                if board._last_symbol == 'X':
                    board1.add_pos(possible[1][0], possible[1][1], 'O')
                    board1._last_symbol = 'O'
                else:
                    board1.add_pos(possible[1][0], possible[1][1], 'X')
                    board1._last_symbol = 'X'
                tree.add_child(board1)
            else:
                if board._last_symbol == "O":
                    symbol = "X"
                else:
                    symbol = "O"
                for i in possible.keys():
                    board1 = copy.deepcopy(board)
                    board1._last_symbol = symbol
                    board1.add_pos(possible[i][0], possible[i][1], symbol)
                    tree.add_child(board1)
                for i in tree.children:
                    recursion(i.key, i)

        recursion(self, tree)
        self.tree = tree

    def computer_move(self):
        """
        (BoardSecondEdition) -> NoneType
        Change board, depending on
        computer move.
        """
        cprint('\nComputer move:', 'yellow')
        lst = self.tree.children
        points = []
        for i in lst:
            leaves_lst = []
            for x in i.leaves():
                leaves_lst.append(x.key)
            points.append(self.count_points(leaves_lst))
        self.positions = lst[points.index(max(points))].key.positions
        print(self)

    def cut_tree(self):
        """
        (BoardSecondEdition) -> NoneType
        Choose current subtree,
        assign its value to the board's tree.
        """
        for i in self.tree.children:
            if i.key == self:
                self.tree = i

    def __eq__(self, other):
        """
        (BoardSecondEdition, BoardSecondEdition) -> bool
        Determine if boards are equal.
        """
        if self.positions == other.positions:
            return True
        return False


def main():
    """
    () -> str
    Simulate tic-tack-toe game.
    """
    board = BoardSecondEdition()
    board.person_move()
    board.make_tree()
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
