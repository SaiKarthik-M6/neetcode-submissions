class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hmap = defaultdict(int)

        result = 0
        maxCount = 0 

        for i in nums:
            hmap[i] += 1 

            if hmap[i] > maxCount: 
                result = i
                maxCount = hmap[i]

        return result 


        

