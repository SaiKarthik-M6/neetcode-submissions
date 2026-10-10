class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        numZeros = 0 
        result = 0 
        l = 0 
        r = 0 

        while r < len(nums): 

            if nums[r] == 0: 
                numZeros += 1 

            while numZeros > k: 
                if nums[l] == 0: 
                    numZeros -= 1 
                l += 1 
            result = max(result, r - l + 1 )
            r +=  1

        return result 