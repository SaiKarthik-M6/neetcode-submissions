class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        start = self.binarySearch(nums, target, True)
        end = self.binarySearch(nums, target, False)

        result.append(start)
        result.append(end)

        return result
        
             
    def binarySearch(self, nums, target, boolean): 
        l = 0
        r = len(nums) - 1
        ans = -1
        while l <= r: 
            mid = l + (r - l) // 2 
            if nums[mid] > target: 
                r = mid - 1
            if nums[mid] < target: 
                l = mid + 1 
            if nums[mid] == target: 
                ans = mid
                if boolean == True: 
                    r = mid - 1
                else: 
                    l = mid +  1
        return ans


