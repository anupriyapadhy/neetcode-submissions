class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        fresh=0
        q=deque()
        def backTrack(r,c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c]==0 :
                return            
            q.append([r,c])
            grid[r][c]=2
            fresh-=1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:                    
                    q.append([i,j])
                if  grid[i][j]==1:  
                    fresh+=1
        if fresh<=0:
            return 0
        dis=-1
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1


            dis+=1
        return dis if fresh==0 else -1