def print_board(board):
    for i, row in enumerate(board):
        if i > 0:  # do not print separator over first row
            print('───┼───┼───')
        print(' ' + ' | '.join(row) + ' ')