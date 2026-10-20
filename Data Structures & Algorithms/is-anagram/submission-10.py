class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        h1 = defaultdict(int)
        h2 = defaultdict(int)

        # char : freq
        for c in s:
            h1[c] += 1
        for c in t:
            h2[c] += 1

        return h1 == h2