# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Input: board =
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true


class Solution:
    def is_valid_sudoku(self, board: list[list[int]]) -> bool:
        from collections import defaultdict
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        sub_grid_dict = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue
                if (board[r][c] in row_dict[r] 
                    or board[r][c] in col_dict[c]
                    or board[r][c] in sub_grid_dict[(r//3, c//3)]):
                    return False
                row_dict[r].add(board[r][c])
                col_dict[c].add(board[r][c])
                sub_grid_dict[r//3,c//3].add(board[r][c])
        return True
