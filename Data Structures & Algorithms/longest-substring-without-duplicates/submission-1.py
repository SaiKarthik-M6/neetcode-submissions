class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashset = set() 
        l = 0 
        r = 1 
        count = 0 

        for r in range(len(s)):
            while s[r] in hashset: 
                hashset.remove(s[l])
                l = l + 1 
            hashset.add(s[r])
            count = max(count, r-l+1)

        return count

        

    