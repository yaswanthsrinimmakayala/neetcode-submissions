class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,-num)
        heapq.heappush(self.min_heap, -1*heapq.heappop(self.max_heap))
        m= len(self.max_heap)
        n= len(self.min_heap)
        if len(self.min_heap) > len(self.max_heap):
            val2 = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val2)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            l = -1*heapq.heappop(self.max_heap)
            m = heapq.heappop(self.min_heap)
            ans = (l+m)/2
            heapq.heappush(self.max_heap,-l)
            heapq.heappush(self.min_heap,m)
            return ans
        else:
            ans = -heapq.heappop(self.max_heap)
            heapq.heappush(self.max_heap,-ans)
            return ans
        