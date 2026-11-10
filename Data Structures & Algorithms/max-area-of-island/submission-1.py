class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rowall = len(grid)
        colall = len(grid[0])

        maxArea = 0 
        count = 0 

        def bfs(r,c): 
            count = 1
            q = collections.deque()
            grid[r][c] = 0
            q.append((r,c))
            directions = [[0,1],[1,0],[0,-1],[-1,0]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions: 
                    nr = dr + row 
                    nc = dc + col 

                    if (nr < 0 or nr >= rowall or nc < 0 or nc >= colall or grid[nr][nc] == 0): 
                        continue 

                    q.append((nr,nc)) 
                    grid[nr][nc] = 0 
                    count = count + 1 
            
            return count 
                

        for r in range(rowall): 
            for c in range(colall): 
                if grid[r][c] == 1: 
                    count = bfs(r,c) 
                    maxArea = max(count, maxArea)
                    count = 0 

        return maxArea 

        
