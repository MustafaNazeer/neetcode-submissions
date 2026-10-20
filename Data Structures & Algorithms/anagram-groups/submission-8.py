class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for c in s:
                letters[ord(c) - ord('a')] += 1
            key = tuple(letters)
            hash[key].append(s)
        
        res = []
        for value in hash.values():
            res.append(value)
        return res