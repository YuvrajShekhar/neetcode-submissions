class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_check = []
            for i in range(len(row)):
                if row[i] in row_check:
                    return False
                else:
                    if row[i]!=".":
                        row_check.append(row[i])

        for i in range(9):
            col_check = []
            for j in range(9):
                if board[j][i] in col_check:
                    return False
                elif board[j][i] != ".":
                    col_check.append(board[j][i])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box_check = []

                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] in box_check:
                            return False
                        elif board[r][c] != ".":
                            box_check.append(board[r][c])

        return True
            

            

        

        

        