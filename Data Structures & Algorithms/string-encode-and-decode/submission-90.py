class Solution:

    def encode(self, strs: List[str]) -> str:
        # 2#5#Hello5#World
        numStrs = len(strs)
        res = str(numStrs) + '#'
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    
    def decode(self, s: str) -> List[str]:
        # 2#50#Hello5#World

        def getValue(i):
            l = i
            x = ""
            while s[l] != '#':
                x += s[l]
                l += 1
            return int(x)
        
        numStrs = getValue(0)

        i = len(str(numStrs)) + 1
        res = []
        while len(res) < numStrs:
            length = getValue(i)
            i += len(str(length)) + 1
            word = s[i: length + i]
            res.append(word)
            i += length
        return res