class Solution:
    def isPalindrome(self, s: str) -> bool:

        def isGood(c):
            return c not in " ?,.[]{}()#':!"
        
        def u(c):
            return chr(ord(c) + ord(" ")) if ord("A") <= ord(c) <= ord("Z") else c

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not isGood(s[l]):
                l += 1
            while l < r and not isGood(s[r]):
                r -= 1

            if u(s[l]) != u(s[r]):
                return False
            
            l += 1
            r -= 1
        return True