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

def get_player_move():
    x_coord = int(input("Enter your move's X-coordinate:"))
    y_coord = int(input("Enter your move's Y-coordinate:"))
    return (x_coord, y_coord)

def make_move(board, player_move, player):
    new_board = board
    new_board[player_move[0]][player_move[1]] = player
    return new_board

def valid_move(board, move):
    return board[move[0]][move[1]] is None

def get_winner():
    pass

board = create_board()
while True:
    move = get_player_move()
    if valid_move(board, move):
        board = make_move(board, move, 'X')
        render(board)
    else:
        print('Invalid move!')