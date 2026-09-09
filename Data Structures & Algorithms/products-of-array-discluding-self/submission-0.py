class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [0] * len(nums) 
        postfix = [0] * len(nums)
        result = [0] * len(nums)

        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] * prefix[i-1]  

        print(prefix)

        postfix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = nums[i] * postfix[i+1]

        print(postfix)

        result[0] = postfix[1]
        result[len(nums) - 1] = prefix[len(nums) - 2]
        for i in range(1, len(nums) - 1):
            result[i] = postfix[i+1] * prefix[i-1]

        return result

