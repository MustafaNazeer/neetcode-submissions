class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # Cases:
        #   1) Take nums[i]
        #   2) Dont Take nums[i]

        # Since every element can only be chosen at most once,
        # we can only ever:
        # Take, move i --> valid
        # Take, dont move i --> Causes Duplicates
        # Dont take, move i --> valid
        # Dont tkae, dont move i --> Makes no sense
        nums.sort()
        def backtrack(path, start):
            if sum(path) == target:
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Take
                if sum(path) + nums[i] <= target:
                    path.append(nums[i])
                    backtrack(path, i + 1)
                    path.pop()

        backtrack([], 0)
        return res