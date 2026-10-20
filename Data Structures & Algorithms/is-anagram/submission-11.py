class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = defaultdict(int)
        b = defaultdict(int)

        for c in s:
            a[c] += 1
        for c in t:
            b[c] += 1
        return a == b