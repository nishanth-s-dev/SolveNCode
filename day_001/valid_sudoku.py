# Platform          : Leetcode
# Problem Number    : 36
# Problem Name      : Valid Sudoku
# Problem Topics    : Array, Hashtable, Matrix
# Problem URL       : https://leetcode.com/problems/valid-sudoku/description/


def has_row_duplicate(board):
    for row in board:
        row_set = set()
        for element in row:
            if element == ".":
                continue
            if element in row_set:
                return False
            row_set.add(element)

    return True

def has_column_duplicates(board):
    col_length = len(board[0])
    for col in range(col_length):
        col_set = set()
        for row in board:
            if row[col] == ".":
                continue
            if row[col] in col_set:
                return False
            col_set.add(row[col])
    return True

def has_duplicate_box(board):
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):

            box_set = set()
            for i in range(box_row, box_row + 3):
                for j in range(box_col, box_col + 3):
                    element = board[i][j]
                    if element == ".":
                        continue
                    if element in box_set:
                        return False
                    box_set.add(element)
    return True

def is_valid_sudoku(board):
    return has_row_duplicate(board) and has_column_duplicates(board) and has_duplicate_box(board)

if __name__ == "__main__":
    sudoku_board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
                    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
                    [".", "9", "1", ".", ".", ".", ".", ".", "3"],
                    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
                    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", ".", ".", ".", ".", ".", "2", ".", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    is_valid_sudoku(sudoku_board)
