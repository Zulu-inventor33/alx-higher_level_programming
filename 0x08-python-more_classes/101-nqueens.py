#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys


def init_board(n):
    """Initialze an `n`x`n` sizd chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for rw in range(len(board)):
        for c in range(len(board)):
            if board[rw][c] == "Q":
                solution.append([rw, c])
                break
    return (solution)


def xout(board, row, col):
    """X out spots a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list):current working chessboard.
        row (int): row where a queen was last played.
        col (int): column where a queen was last played.
    """
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for rw in range(row + 1, len(board)):
        board[rw][col] = "x"
    for rw in range(row - 1, -1, -1):
        board[rw][col] = "x"
    # X  all spots diagonally down to the right
    c = col + 1
    for rw in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[rw][c] = "x"
        c += 1
    # X all spots diagonally up to the left
    c = col - 1
    for rw in range(row - 1, -1, -1):
        if c < 0:
            break
        board[rw][c]
        c -= 1
    # X all spots diagonally up to the right
    c = col + 1
    for rw in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[rw][c] = "x"
        c += 1
    # X all spots diagonally down to the left
    c = col - 1
    for rw in range(row + 1, len(board)):
        if c < 0:
            break
        board[rw][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): This is current working chessboard.
        row (int): current working row.
        queens (int): current number of placed queens.
        solutions (list): list of lists of solutins.
    Returns:
        solutins
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
