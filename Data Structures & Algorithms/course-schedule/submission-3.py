class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        indegree = [0] * numCourses
        for u,v in prerequisites:
            indegree[v] += 1
            graph[u].append(v)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish=0
        while q:
            node=q.popleft()
            finish+=1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
 

        return finish==numCourses



        