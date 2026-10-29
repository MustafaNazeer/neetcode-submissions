class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        found = False
        path = set()

        def backtrack(r, c, i):
            nonlocal found
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in path or i >= len(word) or board[r][c] != word[i]:
                return
            if i == len(word) - 1:
                found = True
                return
            
            path.add((r, c))
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dr, dc in directions:
                backtrack(r + dr, c + dc, i + 1)
            path.remove((r, c))
                

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    backtrack(r, c, 0)
                if found:
                    return True
        return False