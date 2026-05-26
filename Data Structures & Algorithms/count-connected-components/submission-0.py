class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for i in range(n)]
        visit=set()
        res=0        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(i):
            q=deque([i])
            while q:
                curr=q.popleft()
                for nei in adj[curr]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
                        dfs(nei)

        for i in range(n):
            if i not in visit:
                
                dfs(i)
                res+=1
        return res

        