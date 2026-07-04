class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        order=[]
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        visit, cycle=set(), set()

        def dfs(crs):
            
            if crs in visit:
                return True  
            if crs in cycle:
                return False  
            
            cycle.add(crs)
            for pre in adj[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            adj[crs]=[]
            order.append(crs)
            return True

        for crs in range(numCourses):
           if dfs(crs) == False:
                return []

        return order