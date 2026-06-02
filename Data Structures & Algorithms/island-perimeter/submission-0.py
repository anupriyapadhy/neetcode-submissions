class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        perimeter = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                        nr, nc = r + dr, c + dc

                        if (
                            nr < 0 or nr >= ROWS or
                            nc < 0 or nc >= COLS or
                            grid[nr][nc] == 0
                        ):
                            perimeter += 1

        return perimeter