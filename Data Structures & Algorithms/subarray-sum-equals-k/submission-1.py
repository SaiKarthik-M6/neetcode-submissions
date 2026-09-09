class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        curSum = 0 
        count = 0 
        diffMap = {0: 1}

        for n in nums: 
            curSum += n
            diff = curSum - k 

            count += diffMap.get(diff, 0)
            diffMap[curSum] = 1 + diffMap.get(curSum, 0)

        return count