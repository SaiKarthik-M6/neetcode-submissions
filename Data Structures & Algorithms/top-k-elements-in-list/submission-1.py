class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # dictionary: counts -> value  since we need an array the length of the elements in the array  

        # should i use a heap here or a hashmap

        size = len(nums) + 1


        freq = defaultdict(int)
        bucket = [[] * size for _ in range(size)]  
        result = []

        for i in range(len(nums)):  # O(n)
            freq[nums[i]] += 1 

        for key, value in freq.items(): 
            bucket[value].append(key)

        for i in range(len(bucket)-1, 0, -1):
            for val in bucket[i]:
                result.append(val)
                if len(result) == k:
                    return result  
        
        return result




        