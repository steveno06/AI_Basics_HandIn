"""
Tic Tac Toe Player
"""

import math
import copy
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
    xcount = 0
    ocount = 0
    for x in range(3):
        for y in range(3):
            if(board[x][y] ==  X):
                xcount = xcount + 1
            if(board[x][y] ==  O):
                ocount = ocount + 1

    if (xcount > ocount):
        return O
    elif xcount == ocount:
        return X
    else: 
        return None

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    
    for x in range(3):
        for y in range(3):
            if(board[x][y] ==  EMPTY):
                actions.add((x,y))    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        print(action)
        raise ValueError
    elif action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise ValueError
    else:
        newboard = copy.deepcopy(board)
        newboard[action[0]][action[1]] = player(newboard)
        return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    flag = False
    for x in range(3):
        
        if (board[x][0] == board[x][1] == board[x][2]) and (board[x][0] != None):
            flag = True
            return board[x][0]
        elif (board[0][x] == board[1][x] == board[2][x]) and (board[0][x] !=None):
            flag = True
            return board[0][x]
    
    
    if (board[0][0] == board[1][1] == board [2][2]) and (board[0][0] !=None):
        flag = True
        return board[0][0]
    elif (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] !=None):
        flag = True
        return board[0][2]
    
    if flag == False:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    iscomplete = True
    for x in range(3):
        for y in range(3):
            if(board[x][y] == EMPTY):
                iscomplete = False

    
    if(winner(board) != None):
        return True
    
    else:
        return iscomplete

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None
    else:
        p = player(board)

        if p == X:
            v = -1000
            bestaction = None
            for action in actions(board):
                if (min_value(result(board, action))) > v:
                    v = min_value(result(board, action))
                    bestaction = action
            
            return bestaction
        elif p == O:
            v = 1000
            bestaction = None
            for action in actions(board):
                if (max_value(result(board, action))) < v:
                    v = max_value(result(board, action))
                    bestaction = action
            
            return bestaction

def max_value(board):
    if(terminal(board)):
        return(utility(board))
    else:
        v = -1000
        
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

def min_value(board):
    if(terminal(board)):
        return(utility(board))
    v = 1000
    
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
