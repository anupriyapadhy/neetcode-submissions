class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        maxHeap=[]
        for x,y in points:
            distance=x**2+y**2
            heapq.heappush(maxHeap,(-distance,x,y))
            while len(maxHeap)>k:
                heapq.heappop(maxHeap)        
        while len(maxHeap):
             distance,x,y=heapq.heappop(maxHeap)  
             res.append([x,y]) 
        return res
