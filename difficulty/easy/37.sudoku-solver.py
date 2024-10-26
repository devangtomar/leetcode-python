from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle by modifying the board in-place.
        """
        row_dicts = [set() for _ in range(9)]
        col_dicts = [set() for _ in range(9)]
        box_dicts = [set() for _ in range(9)]

        # Pre-fill the sets with the initial numbers from the board
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    row_dicts[i].add(num)
                    col_dicts[j].add(num)
                    box_dicts[(i // 3) * 3 + (j // 3)].add(num)

        def is_valid(row, col, num):
            box_index = (row // 3) * 3 + (col // 3)
            return (
                num not in row_dicts[row]
                and num not in col_dicts[col]
                and num not in box_dicts[box_index]
            )

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in range(1, 10):
                            if is_valid(i, j, num):
                                board[i][j] = str(num)
                                row_dicts[i].add(num)
                                col_dicts[j].add(num)
                                box_dicts[(i // 3) * 3 + (j // 3)].add(num)

                                if solve():
                                    return True

                                # Backtrack
                                board[i][j] = "."
                                row_dicts[i].remove(num)
                                col_dicts[j].remove(num)
                                box_dicts[(i // 3) * 3 + (j // 3)].remove(num)
                        return False
            return True

        solve()
