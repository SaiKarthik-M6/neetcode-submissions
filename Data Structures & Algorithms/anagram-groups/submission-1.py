class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = defaultdict(list)

        for string in strs:
            alpha = [0] * 26  
            for char in string: 
                index = ord(char) - ord('a')
                alpha[index] += 1

            anagram[tuple(alpha)].append(string)

        return list(anagram.values())



