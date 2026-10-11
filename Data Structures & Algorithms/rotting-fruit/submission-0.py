from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        queue = deque()
        countFruit = 0 
        iterations = 0 


        for r in range(row): 
            for c in range(col): 
                if grid[r][c] == 1: 
                    countFruit += 1
                if grid[r][c] == 2: 
                    queue.append([r,c])


        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue and countFruit > 0: 
            for i in range(len(queue)): 
                r,c = queue.popleft()

                for dr, dc in directions: 
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1: 
                        grid[nr][nc] = 2
                        countFruit -= 1
                        queue.append([nr,nc])

            iterations += 1 


        if countFruit > 0: 
            return -1 

        return iterations