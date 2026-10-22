class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            delim = s.find('#', i)
            length = int(s[i:delim])
            word = s[delim + 1 : delim + 1 + length]
            res.append(word)
            i = delim + 1 + length
        return res