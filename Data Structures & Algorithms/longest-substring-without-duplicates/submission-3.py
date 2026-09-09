class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashset = set()

        l = 0 
        r = 0 
        maxCount = 0 

        for r in range(len(s)):
            while s[r] in hashset: 
                hashset.remove(s[l])
                l += 1 

            hashset.add(s[r])
            maxCount = max(maxCount, r - l + 1)

        return maxCount 

        

