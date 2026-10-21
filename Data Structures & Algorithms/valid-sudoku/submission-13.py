class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        tiles = [set() for i in range(9)]

        for r in range(ROWS):
            for c in range(COLS):
                cell = board[r][c]
                if cell == ".":
                    continue

                tileIndex = (r // 3) * 3 + (c // 3)

                if (cell in rows[r] or cell in cols[c] or cell in tiles[tileIndex]):
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                tiles[tileIndex].add(cell)
        return True