class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        result = []
        for i in nums:
            hm[i] = hm.get(i,0)+1
        sorted_items = sorted(
            hm.items(),
            key= lambda x:x[1],
            reverse= True
        )
        return [num for num,count in sorted_items[:k]]

