from data import data

split_input = data.split("\n")

def convert_FB(string):
    translation_table = string.maketrans("FB", "01")
    return string.translate(translation_table)


def convert_LR(string):
    translation_table = string.maketrans("LR", "01")
    return string.translate(translation_table)

binary_columns = [convert_LR(line[-3:]) for line in split_input]
decimal_columns = [int(binary_column, 2) for binary_column in binary_columns]

decimal_rows_and_columns = zip([int(binary_row, 2) for binary_row in [convert_FB(line[:7]) for line in split_input]], decimal_columns)
seat_ids = [item[0] * 8 + item[1] for item in decimal_rows_and_columns]

print(max(seat_ids))
