class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## bit manipulation
        n = len(nums)-1
        res = 0
        num_bits = n.bit_length()
        for b in range(num_bits):
            x,y = 0,0
            for num in nums:
                if (num>>b) & 1:
                    x+=1
            for val in range(1,n+1):
                if (val>>b) & 1:
                    y+=1
            if x>y:
                res = res | (1<<b)
        return res