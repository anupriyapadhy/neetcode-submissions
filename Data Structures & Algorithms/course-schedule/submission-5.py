class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap=defaultdict(list)
        indegree=[0]*numCourses
        for crs, dst in prerequisites:
            indegree[dst]+=1
            preMap[crs].append(dst)
        q=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        finish=0
        while q:
            crs=q.popleft()
            finish+=1
            for nei in preMap[crs]:
                             
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)

        return finish==numCourses

        


        
