from models.board import Board

def test_no_winner():
    board = Board()
    assert board.check_winner() == "", "Empty board no winner"

def test_row_winner():
    board = Board()
    board.update_board(0, 0, 'X')
    board.update_board(0, 1, 'X')
    board.update_board(0, 2, 'X')
    assert board.check_winner() == 'X', "Row winner not detected"

def test_diagonal_winner():
    board = Board()
    board.update_board(0, 0, 'O')
    board.update_board(1, 1, 'O')
    board.update_board(2, 2, 'O')
    assert board.check_winner() == 'O', "Diagonal winner not detected"