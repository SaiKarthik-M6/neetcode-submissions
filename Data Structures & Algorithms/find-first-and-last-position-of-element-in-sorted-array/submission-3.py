class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(nums, target, left):
            l = 0 
            r = len(nums) - 1
            ans = -1 
            while l <= r: 
                mid = l + (r - l) // 2  
                if target < nums[mid]:
                    r = mid - 1
                if target > nums[mid]: 
                    l = mid + 1 
                if target == nums[mid]:
                    ans = mid
                    if left == True:
                        r = mid - 1 
                    else: 
                        l = mid + 1  
        
            return ans

        result = []
        left = binarySearch(nums, target, True)
        right = binarySearch(nums, target, False)

        result.append(left)
        result.append(right)

        return result 
