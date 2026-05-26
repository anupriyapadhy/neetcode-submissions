class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order=[]
        pre=defaultdict(list)
        for i,j in prerequisites:
            pre[i].append(j)
        visit=set()
        UNVISITED,VISITING,VISITED=0,1,2
        states=[UNVISITED]*numCourses
        def dfs(i):
            state=states[i]
            if state==VISITED: return True
            if state==VISITING : return False
            states[i]=VISITING
            for neigh in pre[i]:
                if not dfs(neigh):return False
            states[i]=VISITED
            order.append(i)
            return True

        for neigh in range(numCourses):
            if not dfs(neigh):return []
        return order