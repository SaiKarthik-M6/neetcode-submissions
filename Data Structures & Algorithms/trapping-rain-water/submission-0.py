class Solution:
    def trap(self, height: List[int]) -> int:
        
        lArray = []
        rArray = []

        maxl = 0 
        maxr = 0 

        for num in height: 
            maxl = max(maxl, num)
            lArray.append(maxl)

        for num in reversed(height):
            maxr = max(maxr, num)
            rArray.append(maxr)

        rArray.reverse()
        # min(l, r) - height[i]

        water = 0 

        for i in range(len(height)):
            waterT = min(lArray[i], rArray[i]) - height[i]
            
            if waterT < 0: 
                continue 
            else:
                water = waterT + water

        return water