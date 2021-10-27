def convert_user_input(chess_notation) -> tuple[int, int]:
    column = chess_notation[0].lower()
    row = chess_notation[1]
    
    column_mapping = {'a': 0, 'b': 1, 'c': 2}
    row_mapping = {'3': 0, '2': 1, '1': 2}
    return row_mapping[row], column_mapping[column]