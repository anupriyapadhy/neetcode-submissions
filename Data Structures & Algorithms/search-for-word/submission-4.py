class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board), len(board[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(r,c,i):
            if i == len(word):
                return True
            if r not in range(rows) or c not in range(cols):
                return False
            if board[r][c] != word[i]:
                return False
            temp=board[r][c]
            board[r][c]='#'
            found=False
            for nr, nc in directions:
                newRow, newCol=r+nr, c+nc   
                if dfs(newRow, newCol,i+1):
                    found=True
                    break         
            board[r][c]=temp
            return found

        for r in range(rows):
            for c in range(cols):                
                if dfs(r,c,0):
                    return True
        return False

        