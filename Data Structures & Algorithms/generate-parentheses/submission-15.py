class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        # All cases:
        #   1) opened == n and closed == n --> base case
        #   2) opened == n and closed < n --> ALWAYS ")"
        #   4) opened < n and closed < n
        #       a) opened == closed --> ALWAYS "("
        #       c) opened > closed --> Either one


        def backtrack(path, opened, closed):
            if opened == n and closed == n:
                res.append(path)
                return

            if opened == n and closed < n:
                path += ")"
                backtrack(path, opened, closed + 1)
                path = path[:-1]
            
            if opened < n and opened == closed:
                path += "("
                backtrack(path, opened + 1, closed)
                path = path[:-1]
            
            if opened < n and opened > closed:
                path += ")"
                backtrack(path, opened, closed + 1)
                path = path[:-1]

                path += "("
                backtrack(path, opened + 1, closed)
                path = path[:-1]

        backtrack("", 0, 0)
        return res