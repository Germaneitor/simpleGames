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
    x_coord = int(input("Enter your move's X-coordinate: "))
    y_coord = int(input("Enter your move's Y-coordinate: "))
    return (x_coord, y_coord)

def make_move(board, player_move, player):
    new_board = board
    new_board[player_move[0]][player_move[1]] = player
    return new_board

def valid_move(board, move):
    return board[move[0]][move[1]] is None

def get_winner(board):
    rows = [board[0][:],
            board[1][:],
            board[2][:]]
    columns = [[row[0] for row in board],
               [row[1] for row in board],
               [row[2] for row in board]]
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    print(rows + columns + diagonals)
    return rows + columns + diagonals

def check_draw(board):
    for row in board:
        for col in row:
            if col is None:
                return False
    return True

def start_game():
    turn = 1
    board = create_board()
    render(board)
    players = ['O', 'X']
    while True:
        print("Your turn player", players[turn % 2])
        move = get_player_move()
        if valid_move(board, move):
            board = make_move(board, move, players[turn % 2])
            render(board)
        else:
            print('Invalid move!')
            continue
        
        if ['X', 'X', 'X'] in get_winner(board):
            print("X player wins!")
            break
        elif ['O', 'O', 'O'] in get_winner(board):
            print("O player wins")
            break
        elif check_draw(board):
            print("It is a draw!")
            break
        turn += 1

if __name__ == '__main__':
    start_game()