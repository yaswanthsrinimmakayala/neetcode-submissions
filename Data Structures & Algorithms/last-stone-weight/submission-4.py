class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        heap = [-1*s for s in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            x = -1*heapq.heappop(heap)
            y = -1*heapq.heappop(heap)
            if x==y:
                continue
            else:
                x = x-y
                heapq.heappush(heap,-1*x)
        return -1*heap[0] if heap else 0
