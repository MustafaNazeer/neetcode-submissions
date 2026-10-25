class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        #  Cases:
        # sum(path) > target --> ignore
        # sum(path) == target --> Base Case
        # sum(path) < target
        #   Take, move i
        #   Take, leave i
        #   dont take, move i

        # Take, move i
        # Take, leave i
        # dont take, move i

        def backtrack(path, i):
            if sum(path) == target:
                res.append(path[:])
                return
            
            if i < len(nums) and sum(path) + nums[i] <= target:
                path.append(nums[i])
                backtrack(path, i) # take, dont move i
                path.pop()
            if i < len(nums):
                backtrack(path, i + 1) # dont take, move i

        backtrack([], 0)
        return res