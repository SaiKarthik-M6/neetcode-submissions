class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        map = defaultdict(int)
        bucket = defaultdict(list)

        for i in range(len(nums)): 
            map[nums[i]] += 1 

        for key, token in map.items():
            bucket[token].append(key)

        res = []
        for freq in range(len(nums), 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res
