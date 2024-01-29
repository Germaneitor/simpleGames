def welcome():
    print("Welcome to Tic-Tac-Toe")
    user_help = input("If you'd like to know how to play, type 'help'. Otherwise, press Enter.\n")
    if user_help == 'help':
        print("In this game, you select where to place your move on the following board.",
              "This positions are as coordintes (x, y). with x being the row, and y the column.\n" +
              "If you try to place a move in a filled space, you need to try again.\n")
    print("Enjoy!\n")

def check_board(board):
    return check_diagonals(board) or check_columns(board) or check_rows(board)

def check_diagonals(board):
    # Diagonals in both directions
    diagonal_lr = [board[0][0], board[1][1], board[2][2]]
    diagonal_rl = [board[0][2], board[1][1], board[2][0]]
    # Check if either diagonal is filled with X or O
    if diagonal_lr.count('X') == 3 or diagonal_lr.count('O') == 3:
        return True
    if diagonal_rl.count('X') == 3 or diagonal_rl.count('O') == 3:
        return True
    
    return False

def check_columns(board):
    columns = [{row[0] for row in board}, 
               {row[1] for row in board}, 
               {row[2] for row in board}]
    
    for col in columns: # Check if any column has the winning player
        if 'X' in col and len(col) == 1:
            return True
        if 'O' in col and len(col) == 1:
            return True
    
    return False

def check_rows(board):
    rows = [board[0][:],
            board[1][:],
            board[2][:]]
    
    for row in rows:
        if row.count('X') == 3 or row.count('O') == 3:
            return True
    return False

def player_moves(player, board):
    print('\n'.join(('\t'.join([cell for cell in row]) for row in board)))
    user_move = input(f"Player {player}, type your coordinates. Formatted as: x,y\n")
    return int(user_move.split(',')[0]), int(user_move.split(',')[1])

def main():
    welcome()
    board = [['-', '-', '-'],
             ['-', '-', '-'],
             ['-', '-', '-']]
    player = 1
    turns = 1
    while True:
        if check_board(board): # Check the moves so far for a winner
            if player == 1: # Make sure we have the correct winner
                player = 2
            player = 1
            print(f"Player {player} wins!\n")
            print('\n'.join(('\t'.join([cell for cell in row]) for row in board)))
            break

        x, y = player_moves(player, board) # Get the player's move coordinates
        if board[x][y] == 'X' or board[x][y] == 'O':
            print("Invalid move, select new position.\n")
            continue
        
        if player == 1:
            board[x][y] = 'X'
            turns += 1
            player = 2
            continue
        board[x][y] = 'O'
        turns += 1
        player = 1

        if turns == 10:
            break

if __name__ == "__main__":
    main()