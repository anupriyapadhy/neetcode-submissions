class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()
        fresh=0

        def addCell(r, c):
            nonlocal fresh
            if (min(r, c) >=0  and r < ROWS and c < COLS 
                 and grid[r][c] == 1
            ):
                
                fresh-=1
                grid[r][c] = 2            
                q.append([r, c])


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:                    
                    q.append([r, c])                    
                elif grid[r][c] == 1:
                    fresh+=1   

        time = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()

                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)

            time += 1


        return time if fresh == 0 else -1        