class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph=defaultdict(int)
        
        for u,v in trust:
            graph[u]-=1
            graph[v]+=1

        for i in range(1,n+1):
            if graph[i]==n-1:
                return i
        

        return -1