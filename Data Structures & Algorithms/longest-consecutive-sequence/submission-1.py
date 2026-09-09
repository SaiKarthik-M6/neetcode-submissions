class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if(len(nums) == 0):
            return 0

        sortedNum = nums.sort()
        maxConsec = 1
        consec = 1

        for i in range(len(nums)-1):
            if (nums[i+1] == nums[i] + 1): 
                consec = consec + 1 
                maxConsec = max(maxConsec, consec)
            elif (nums[i+1] == nums[i]):
                continue
            else:
                consec = 1

        return maxConsec 

        [2,3,4,5,10,20]