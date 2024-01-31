# tic-tac-toe with potential AI players

def create_board():
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        return board

def render(board):
    print("   0 1 2")
    print("   ------")
    for row in range(3):
        line = str(row) + ' |'
        for col in range(3):
             line += '  ' if board[col][row] == None else board[col][row] + ' '
        line += '|'
        print(line)
    print("   ------")

def get_winner():
    pass

board = create_board()
board[0][1] = 'X'
board[1][1] = 'O'
render(board)