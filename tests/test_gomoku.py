from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from gomokuGame import create_board, is_valid_move, make_move, check_winner


def test_create_board_size_and_default_cell():
    board = create_board(15)
    assert len(board) == 15
    assert all(len(row) == 15 for row in board)
    assert all(cell == '-' for row in board for cell in row)


def test_is_valid_move_rejects_occupied_cell():
    board = create_board(15)
    make_move(board, 7, 7, 'X')
    assert is_valid_move(board, 7, 7) is False


def test_check_winner_horizontal_five_in_row():
    board = create_board(15)
    row = 3
    for col in range(5):
        make_move(board, row, col, 'X')

    assert check_winner(board, 'X') is True
