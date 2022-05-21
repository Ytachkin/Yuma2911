"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, -],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""


from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    >>> tic_tac_toe_checker([['x', '0', '0'],['x', '0', 'x'],['x', 'x', '0']])
    'x wins'
    >>> tic_tac_toe_checker([['0', '0', '0'],['x', '0', 'x'],['x', 'x', '0']])
    '0 wins'
    >>> tic_tac_toe_checker([['-', '0', '0'],['x', '0', '-'],['x', 'x', '0']])
    'the board is unfinished'
    >>> tic_tac_toe_checker([['0', '0', 'x'],['x', 'x', '0'],['0', 'x', '0']])
    "it's a draw"
    """
    who = ''
    res = False
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            res = True
            who = board[i][0]
            break
        if board[0][i] == board[1][i] == board[2][i]:
            res = True
            who = board[0][i]
            break

    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        res = True
        who = board[1][1]

    if res:
        return f'{who} wins'
    else:
        joined_list = board[0] + board[1] + board[2]
        if '-' in joined_list:
            return 'the board is unfinished'
        else:
            return "it's a draw"