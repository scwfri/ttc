"""Simple Tic Tac Toe game written, its called Ttc!"""

import random
from typing import NamedTuple


BOARD_SIZE = 3


class Point(NamedTuple):
    """To store point of next move"""

    column: str
    row: int

    def __repr__(self):
        return str(self.column) + str(self.row)

    def get_column(self) -> int:
        """Returns column number - 0 indexed"""

        return ord(self.column) - 97

    def get_row(self) -> int:
        """Returns row number - visual board is 1 indexed, so converts to 0-index"""

        return int(self.row)-1


class Aimee:
    """(AI)mee is the AI class you will play againstQ"""

    # TODO: make her intelligent

    def __init__(self, player: str):
        self.player = player

    def get_player(self) -> str:
        """returns player representaion (i.e. X or O)"""

        return self.player

    def get_move(self, board) -> Point:
        """get Aimee to return a move"""

        # winning_move = self.find_winning_move(board)

        column = chr(random.randint(0, BOARD_SIZE) + 96)
        row = random.randint(0, BOARD_SIZE)
        return Point(column=column.lower(), row=row)

    def find_winning_move(self, board) -> Point:
        """Find a winning move, if there is one"""

        horizontal_winner = find_horizontal_winner(board)
        # vertical_winner = find_vertical_winner(board)
        # diagonal_winner = find_diagonal_winner(board)

        if horizontal_winner is not None:
            return horizontal_winner
        # elif vertical_winner is not None:
            # return vertical_winner
        # elif diagonal_winner is not None:
            # return diagonal_winner
        return None

    def find_horizontal_winner(self, board) -> Point:
        """Find horizontal winner"""

        pass

def find_horizontal_winner(board) -> Point:
    """Find horizontal winner"""

    for i, row in enumerate(board):
        if row[0] == row[1] == 'O' and row[2] is None:
            print("found winner -- %s, 2" %(i))
            return Point(column='c', row=i)
        if row[1] == row[2] == 'O' and row[0] is None:
            print("found winner -- %s, 0" %(i))
            return Point(column='a', row=i)
        if row[0] == row[2] == 'O' and row[1] is None:
            print("found winner -- %s, 1" %(i))
            return Point(column='b', row=i)
    print("did not find horizontal winner")
    return None

def find_vertical_winner(board) -> Point:
    """Find vertical winner"""

    pass

def find_diagonal_winner(board) -> Point:
    """Find diagonal winner"""

    pass

def run_ttc():
    """run TTC game"""

    board = create_board(BOARD_SIZE)
    current_player_is_user = True #TODO: determine what value user wants to be
    num_valid_moves = 0
    opponent = Aimee("O")
    is_winner = False

    print_board(board)

    def get_current_player() -> str:
        """Returns current player -- either 'X' or 'O'"""

        if current_player_is_user:
            return 'X'
        return 'O'

    while num_valid_moves < 9:
        if current_player_is_user:
            point = get_move(get_current_player())
        else:
            point = opponent.get_move(board)
        if point is not None:
            valid = is_valid_move(board, point)
            if valid:
                num_valid_moves += 1
                c_player = get_current_player()
                update_board(board, point, c_player)
                if check_winner(board):
                    is_winner = True
                    if current_player_is_user:
                        print("YOU ARE THE WINNER!!!")
                    else:
                        print("Aimee is the winner!")
                    break
                current_player_is_user = not current_player_is_user
            else:
                if current_player_is_user:
                    print("Invalid move! Please try again...")
    if not is_winner:
        print("It's a DRAW!!!")


def create_board(size):
    """Create the initial board, using size given by the user"""

    board = []

    try:
        for _ in range(0, size):
            tmp = []
            for _ in range(0, size):
                tmp.append(None)
            board.append(tmp)

        return board
    except TypeError:
        print("Invalid board size given")


def is_valid_move(board, point: Point) -> bool:
    """determines if move is valid (i.e. there is no point on board yet)"""

    try:
        move_column = point.get_column()
        move_row = point.get_row()
        return point_is_none(board, move_column, move_row)
    except (IndexError, ValueError):
        return False


def update_board(board, point: Point, player: str):
    """update board to reflect most recent move"""

    board[point.get_row()][point.get_column()] = player
    print_board(board)


def check_horizontal_winner(board) -> bool:
    """checks for horizontal winner"""

    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return True
    return False


def check_vertical_winner(board) -> bool:
    """checks for vertial winner"""

    for column in range(0, BOARD_SIZE):
        """
        board[0][0] == board[0][1] == board[0][2]
        """
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] is not None:
            return True
    return False


def check_diagonal_winner(board) -> bool:
    """checks for diagonal winner"""

    mid = board[1][1]
    if mid is not None:
        if board[0][0] == mid == board[2][2]:
            return True
        if board[2][0] == mid == board[0][2]:
            return True
    return False


def check_winner(board) -> bool:
    """Check if last move created a winner!"""


    is_winner = False

    is_winner |= check_horizontal_winner(board)
    is_winner |= check_vertical_winner(board)
    is_winner |= check_diagonal_winner(board)

    return is_winner


def print_board(board):
    """Print the current board"""

    num = 0
    print()
    print("  ", end="")
    for letter in range(97, 97 + len(board)):
        print('{:^6}'.format(chr(letter)), end="")
    print("")
    for i in board:
        print("%s|"%(num+1), end="")
        num += 1
        for j in i:
            print('{:^5}'.format(str(j)), end="")
            print("|", end="")
        print("")
    print()


def get_move(current_player):
    """Get move from player"""

    print("CURRENT PLAYER: %s" %(current_player))
    move: str = input("Please enter move <column><row>: ")
    try:
        column: str = move[0]
        row: int = move[1]
    except (IndexError, ValueError):
        print("Invalid move! Please try again...")
        return None
    return Point(column=column.lower(), row=row)


def point_is_none(board, column: int, row: int) -> bool:
    """Determine if board is "None" at given row and column"""

    if board[row][column] is None:
        return True
    return False


if __name__ == "__main__":
    run_ttc()