class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        index = defaultdict(int)

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if index[diff]:
                return [index[diff], i + 1]
            
            index[numbers[i]] = i + 1

        return []        




