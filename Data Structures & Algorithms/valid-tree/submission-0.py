class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        graph=defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()
        q = deque([(0, -1)])  # (current node, parent node)
        visit.add(0)


        while q:
            sourceNode, parentNode=q.popleft()

            for nei in graph[sourceNode]:
                if nei==parentNode:
                    continue
                if nei in visit:
                    return False
                visit.add(nei)

                q.append((nei, sourceNode))

        return len(visit) == n


        

        