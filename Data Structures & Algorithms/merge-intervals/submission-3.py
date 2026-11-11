class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        output = [intervals[0]]

        for start, end in intervals[1:]: 
            endstart = output[-1][1]

            if start <= endstart: 
                output[-1][1] = max(end, endstart)
            else: 
                output.append([start,end])

        return output
        