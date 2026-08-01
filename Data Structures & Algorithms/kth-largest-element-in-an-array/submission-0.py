class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = [-i for i in nums]
        heapq.heapify(num)
        while k>0:
            res = heapq.heappop(num)
            k-=1
        return -1*res