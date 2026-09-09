class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False 
        
        setT = defaultdict(int)
        setS = defaultdict(int)

        for i in range(len(s)):
            setT[s[i]] += 1
            setS[t[i]] += 1



        if setT == setS: 
            return True 
        else:
            return False




