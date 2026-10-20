from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h1 = Counter(s)
        h2 = Counter(t)

        return h1 == h2