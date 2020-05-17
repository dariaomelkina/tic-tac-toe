# based on recommendations from consultation (15.05.2020)
# required: pip install termcolor
import random
import copy
from btree import LLBinaryTree
from termcolor import colored, cprint


class Board:
    """ Class for board representation. """

    def __init__(self):
        """
        (Board) -> NoneType
        Create new board.
        """
        self.positions = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self._last_symbol = None

    def state(self):
        """
        (Board) -> str/NoneType
        Return state of the board.
        """
        for i in self.positions:
            if i.count('O') == 3:
                return 'O'
            elif i.count('X') == 3:
                return 'X'
        for x in range(3):
            flag = []
            for y in self.positions:
                flag.append(y[x])
            if flag.count('O') == 3:
                return 'O'
            elif flag.count('X') == 3:
                return 'X'

        if [self.positions[0][0], self.positions[1][1], self.positions[2][2]].count('O') == 3:
            return 'O'
        elif [self.positions[0][0], self.positions[1][1], self.positions[2][2]].count('X') == 3:
            return 'X'

        if [self.positions[0][2], self.positions[1][1], self.positions[2][0]].count('O') == 3:
            return 'O'
        elif [self.positions[0][2], self.positions[1][1], self.positions[2][0]].count('X') == 3:
            return 'X'

        if not self.possible():
            return 'XO'

    def possible(self):
        """
        (Board) -> dictionary
        Return dictionary of possible moves.
        """
        dct = dict()
        for x in range(3):
            for y in range(3):
                if self.positions[x][y] is 0:
                    if dct.keys():
                        key = max(dct.keys()) + 1
                    else:
                        key = 1
                    dct[key] = (x, y)
        return dct

    def person_move(self):
        """
        (Board) -> NoneType
        Accept input from the user,
        add user's move to the positions.
        """
        dct = self.possible()
        cprint('Current possible moves: ' + str(dct), 'magenta')
        move = int(input(colored('Choose a move: ', 'magenta')))
        while move not in dct.keys():
            try:
                raise NotAllowedMoveException
            except NotAllowedMoveException:
                move = int(input(colored('Sorry, that move is not possible. Choose another one: ', 'magenta')))
        self.add_pos(dct[move][0], dct[move][1], 'X')
        self._last_symbol = 'X'
        cprint('\nYour move:', 'cyan')
        print(self)

    def __str__(self):
        """
        (Board) -> str
        Return string representation of the board.
        """
        st = '  | 0 | 1 | 2   \n––––––––––––––\n'
        for i in range(3):
            st += '{} '.format(i)
            for y in range(3):
                if self.positions[i][y] == 0:
                    element = ' '
                else:
                    element = self.positions[i][y]
                    if element == 'X':
                        element = colored(element, 'cyan')
                    else:
                        element = colored(element, 'yellow')
                st += '| ' + str(element) + ' '
            st += '\n––––––––––––––\n'
        return st

    def tree(self):
        """
        (Board) -> Board
        Choose the best variant out of two,
        by building binary tree.
        """
        tree = LLBinaryTree(self.positions)

        def recursion(board, tree):
            possible = board.possible()

            if len([i for i in possible.keys()]) < 2:
                board1 = copy.deepcopy(board)
                if self._last_symbol == 'X':
                    board1.add_pos(possible[1][0], possible[1][1], 'O')
                else:
                    board1.add_pos(possible[1][0], possible[1][1], 'X')
                tree.insert_left(board1)
            else:
                x = random.choice([i for i in possible.keys()])
                new_move1 = possible[x]
                del possible[x]
                new_move2 = possible[random.choice([i for i in possible.keys()])]

                board1 = copy.deepcopy(board)
                board2 = copy.deepcopy(board)

                if self._last_symbol == 'X':
                    nextm = 'O'
                    self._last_symbol = 'O'
                else:
                    nextm = 'X'
                    self._last_symbol = 'X'
                board1.add_pos(new_move1[0], new_move1[1], nextm)
                board2.add_pos(new_move2[0], new_move2[1], nextm)

                tree.insert_left(board1)
                tree.insert_right(board2)

                recursion(board1, tree.get_left())
                recursion(board2, tree.get_right())

        recursion(self, tree)

        left_tree_points = self.count_points(tree.left.get_leaves())
        right_tree_points = self.count_points(tree.right.get_leaves())

        if left_tree_points > right_tree_points:
            return tree.left.key
        else:
            return tree.right.key

    @staticmethod
    def count_points(lst):
        """
        (lst) -> int
        Count points depending on the results of the game,
        finished with such boards.
        """
        result = 0
        for i in lst:
            if i.state() == "X":
                result -= 1
            elif i.state() == "O":
                result += 1
        return result

    def add_pos(self, x, y, item):
        """
        (Board) -> NoneType
        Add item to a (x, y) position.
        """
        self.positions[x][y] = item

    def computer_move(self):
        """
        (Board) -> NoneType
        Change board, depending on
        computer move.
        """
        self.positions = self.tree().positions
        cprint('\nComputer move:', 'yellow')
        print(self)


class NotAllowedMoveException(Exception):
    """ Class for not allowed move represenation. """
    pass
