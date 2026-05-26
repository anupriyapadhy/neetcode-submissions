class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols=len(grid),len(grid[0])
        visited=set()
        islands=0
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        def bfs(r,c):
            q=deque([(r,c)])            
            visited.add((r,c))
            while q:
                row,col=q.popleft()
                for dr in directions:                   
                    nr, nc = row + dr[0], col + dr[1]
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc]=="1" and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))

            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands
        