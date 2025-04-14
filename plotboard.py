"""
board[x][y] gives x and y coords, x is top down, y is left to righ
board[0][0] is top left
board[1][0] is under topleft
board[0][1] is right of topleft
0 means empty, 1 means player 1, 2 means player 2
"""
# display board prints out pretty board
def display_board(board):
    for i in range(len(board)):
        print("|", end=" ")
        for j in range(len(board[i])):
            if board[i][j] == 0:
                print(" |", end=" ")
            elif board[i][j] == 1:
                print("X|", end=" ")
            else:
                print("O|", end=" ")
        print()
# make_move makes a move and returns the new board
def make_move(board,slot,player):
    optionset = options(board)
    if slot not in optionset:
        raise ValueError("Invalid move, slot full")
    y = slot
    for i in range(5,0,-1):
        if board[i][y] == 0:
            board[i][y] = player
            break
    return board

# checkover checks if the game is over and returns the winner
# options gives possible moves
def options(board):
    optionset = []
    for i in range(len(board[0])):  # Iterate over columns
        if board[0][i] == 0:  # Check if the top row of the column is empty
            optionset.append(i)
    return optionset
# play makes a move and returns the new board
# think returns the best move for the AI
