class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n,visited=len(grid),len(grid[0]),set()
        q=deque()
        def backTrack(r,c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c]==-1 or (r,c) in visited:
                return
            visited.add((r,c))
            q.append([r,c])
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    visited.add((i,j))
                    q.append([i,j])
        dis=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dis
                backTrack(r-1,c)
                backTrack(r+1,c)
                backTrack(r,c-1)
                backTrack(r,c+1)
            dis+=1

        