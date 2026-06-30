class Solution:
    def hours_needed(self,k,piles):
        total = 0
        for pile in piles:
            total += pile//k + (1 if pile%k!=0 else 0)
        return total
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        # result = 0
        while low<=high:
            mid = (low+high)//2
            if self.hours_needed(mid,piles)<=h:
                result = mid
                high = mid-1
            else:
                low = mid+1
        return result