class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            
        result = []
        string = defaultdict(list)


        for i in range(len(strs)):
            sortedStr = "".join(sorted(strs[i]))
            string[sortedStr].append(strs[i])

        for key, value in string.items():
            result.append(value)

        return result 