class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            
            # take nums[i]
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

            # dont take nums[i]
            backtrack(i + 1, path)
        
        backtrack(0, [])
        return res