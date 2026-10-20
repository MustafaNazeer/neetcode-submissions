class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        postfix = [1] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] * nums[i]
        for i in range(len(nums))[::-1]:
            postfix[i] = postfix[i + 1] * nums[i]
        
        res = [1] * (len(nums))
        for i in range(len(nums)):
            res[i] = prefix[i] * postfix[i + 1]
        return res