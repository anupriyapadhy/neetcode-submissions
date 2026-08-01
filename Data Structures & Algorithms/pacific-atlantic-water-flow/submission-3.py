class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS= len(heights), len(heights[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        output=[]
        pacific=set()
        atlantic=set()
        
        def dfs(r,c,visit, prevHeight):
            if (r,c) in visit or r not in range(ROWS) or c not in range(COLS) or heights[r][c] < prevHeight :
                return 
            
            visit.add((r,c))
            for dr,dc in directions:
                nr, nc=r+dr, c+dc                                    
                dfs(nr,nc, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    output.append([r,c])
                    
        return output