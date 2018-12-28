"""Test suite for Ttc"""


from ttc.ttc import *


def test_board_size():
    """test board size is correct"""

    # test if valid board size
    board = create_board(3)
    assert len(board) == 3


def test_find_horizontal_winner():
    """test find_horizontal_winner"""

    # test if solution
    solution_board = []
    solution_board.append(['O', 'O', None])
    solution_board.append([None, None, None])
    solution_board.append([None, None, None])

    assert find_horizontal_winner(solution_board) == Point(column='c', row=0)

    # test if no solution
    no_solution_board = []
    no_solution_board.append([None, None, None])
    no_solution_board.append([None, None, None])
    no_solution_board.append([None, None, None])
    assert find_horizontal_winner(no_solution_board) is None


def test_aimee_player():
    """Make sure AImee knows correct player"""

    aimee = Aimee('O')

    assert aimee.get_player() == 'O'