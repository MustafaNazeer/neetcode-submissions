class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isGood(c):
            return c not in " ?,.[]{}()#':!"

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not isGood(s[l]):
                l += 1
            while l < r and not isGood(s[r]):
                r -= 1

            if s[l].upper() != s[r].upper():
                return False
            
            l += 1
            r -= 1
        return True