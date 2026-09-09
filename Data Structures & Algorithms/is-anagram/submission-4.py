class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False

        str1 = defaultdict(int)
        str2 = defaultdict(int)

        for i in s: 
            if i in str1:
                str1[i] = str1[i] + 1 
            else: 
                str1[i] = 1 

        for j in t: 
            if j in str2:
                str2[j] = str2[j] + 1 
            else: 
                str2[j] = 1

        if(str1 == str2):
            return True 

        return False 
