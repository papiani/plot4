from plotboard import *
# initialise board
board = [[0 for i in range(7)] for j in range(6)]
# board[x][y] gives coords
display_board(board)
player = 2
while True:
    if player == 1:
        player = 2
    elif player == 2:
        player = 1
    user_input = int(input("Enter a column number (1-7): ")) - 1
    make_move(board,user_input,player)
    display_board(board)
    





