class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        tiles = [set() for i in range(9)]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                
                tileIndex = (r // 3) * 3 + (c // 3)

                if (board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in tiles[tileIndex]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                tiles[tileIndex].add(board[r][c])

        return True
        