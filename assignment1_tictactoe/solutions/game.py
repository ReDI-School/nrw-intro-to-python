board = create_new_board()
for i in range(9):  # there are 9 fields, so we would expect no game to take more than 9 rounds
    print_board(board)
    user_decision = input('What is your next move?')
    if user_decision == 'stop':
        break
    user_decision_tuple = convert_user_input(user_decision)
    board = update_board(
        board,
        i % 2,
        user_decision_tuple
    )