class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        ROWS, COLS=len(grid), len(grid[0])
        visited=set()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        q=deque()
        fresh=0
        def bfs(r,c):
            nonlocal time
            q.append((r,c))
            visited.add((r,c))
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    fresh += 1
                if grid[r][c]==2 and (r,c) not in visited:
                    q.append((r,c))

        while q and fresh>0:
            for i in range(len(q)):
                row,col=q.popleft()
                for dr in directions:
                    nr,nc= row+dr[0],col+dr[1]
                    if (nr, nc) not in visited and nr in range(0,ROWS) and nc in range(0,COLS) and grid[nr][nc] == 1:
                        grid[nr][nc]=2
                        visited.add((nr,nc))
                        q.append((nr,nc))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1
                    

        