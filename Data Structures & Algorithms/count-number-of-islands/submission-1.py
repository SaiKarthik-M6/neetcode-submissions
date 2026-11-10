class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Row = len(grid)
        Col = len(grid[0])
        numIslands = 0 
            

        def bfs (r, c):
            q = collections.deque()
            q.append((r,c))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            while q: 
                row, col = q.popleft()
                for dr, dc in directions: 
                    nr, nc = dr + row, dc + col 
                    if (nr < 0 or nr >= Row or nc < 0 or nc >= Col or grid[nr][nc] == "0"):
                        continue

                    q.append((nr,nc))
                    grid[nr][nc] = "0"


        for r in range(Row): 
            for c in range(Col): 
                if grid[r][c] == "1": 
                    bfs(r,c)
                    numIslands += 1 

        return numIslands