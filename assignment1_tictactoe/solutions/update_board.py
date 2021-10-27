def update_board(board, player, move):
    row, column = move
    if player == 0:
        piece = 'X'
    else:
        piece = 'O'
    board[row][column] = piece
    return board