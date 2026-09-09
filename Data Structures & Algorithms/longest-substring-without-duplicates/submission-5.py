class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0 
        maxLen = 0

        hashSet = set()

        while r < len(s):
            if s[r] not in hashSet:
                hashSet.add(s[r])
                maxLen = max(maxLen, r - l + 1)
                r += 1 

            else: 
                hashSet.remove(s[l])
                l += 1 

        
        return maxLen

                