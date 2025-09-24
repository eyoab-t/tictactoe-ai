"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
# counts the number moves the players made

    x_move = sum(row.count("X") for row in board)
    o_move = sum(row.count("O") for row in board)   
    

# checks which player has the next turn and returns the player

    # if the game is in initial_state
    if x_move == o_move:
        return X

    if x_move > o_move:
        return O

    if x_move < o_move:
        return X         




def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                possible_actions.add((i, j))
    
    return possible_actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    player_move = player(board)
    new_board = deepcopy(board)

    if not action in actions(board):
        raise Exception("Invaild Action")

    else:
        new_board[i][j] = player_move
    
    return new_board



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]    
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    #if there is no winner
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
#   no possible moves

    if sum(row.count(None) for row in board) == 0:
        return True

#  if there is  a winner

    if winner(board) is not None:
        return True

    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X:
        return 1

    elif winner(board) is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            val = -5
            for action in actions(board):
                min_val = min_value(result(board, action))[0]
                if min_val > val:
                    val = min_val
                    optimal_move = action
            return val, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            val = 5
            for action in actions(board):
                max_val = max_value(result(board, action))[0]
                if max_val < val:
                    val = max_val
                    optimal_move = action
            return val, optimal_move



    current_player = player(board)

    if terminal(board):
        return None

    if current_player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]




