class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in s:
            j = 1
            if i - 1 not in s:
                while i + j in s:
                    j += 1
            res = max(res, j) 
        return res