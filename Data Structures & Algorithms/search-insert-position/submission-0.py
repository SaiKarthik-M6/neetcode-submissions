class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1 
        result = len(nums)

        while l <= r: 
            mid = l + (r - l) // 2
            if nums[mid] == target: 
                return mid
            if nums[mid] > target: 
                result = mid
                r = mid - 1
            else: 
                l = mid + 1  
        return result



    # [-1,0,2,4,6,8] 