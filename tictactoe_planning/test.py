from tictactoe import max_value, result, actions, winner, terminal, player

X = "X"
O = "O"
EMPTY = None
board = [[X,    X, X],
            [O, O, X],
            [X, O, X]]



win3 = terminal(board)

print(win3)