# Tic Tac Toe

board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#print (board) print for checking

def display_board(board):
    for row in (board):
        print(f" {row[0]} | {row[1]} | {row[2]}")
        print('__________')

def player_input(player, board):
    while True:
        move_row = int(input(f"Player {player}, enter a row (0, 1, or 2): "))
        while move_row not in range(3):
            move_row = int(input(f"Player {player}, that's invalid! Enter a row (0, 1, or 2): "))
    
        move_column = int(input(f"Player {player}, enter a column (0, 1, or 2): "))
        while move_column not in range(3):
            move_column = int(input(f"Player {player}, that's invalid! Enter a column (0, 1, or 2): "))
        
        if board[move_row][move_column] == ' ':
            return move_row, move_column
        else:
            print("That cell is already taken! Try again.")

def check_win(board, player):
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def check_tie(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def play():
    board = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]
    
    player = 'X'
    
    while True:
        display_board(board)
        row, column = player_input(player, board)
        board[row][column] = player
        
        if check_win(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break
        
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break
        
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

#########################################################################################################################
#Start the game 
#########################################################################################################################

play()