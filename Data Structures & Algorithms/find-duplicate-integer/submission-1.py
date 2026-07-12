class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## binary search
        low = 1
        high = len(nums)-1
        while low < high:
            mid = (low+high)//2

            count = sum(1 for i in nums if i<=mid)
            if count<=mid:
                low = mid+1
            else:
                high = mid
        return low