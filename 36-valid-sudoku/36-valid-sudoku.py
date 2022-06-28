class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in grid[r//3,c//3]:
                        return False
                    # print(row)
                    # print(col)
                    # print(grid)
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    grid[r//3,c//3].add(board[r][c])
        return True