class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cnt = 0 
        product = 1
        res = [0]*len(nums)
        for i in nums:
            if i==0:
                cnt+=1
            else:
                product*=i

        if cnt>1:
            return [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                res[i] = product
            else:
                if cnt==0:
                    res[i] = product//nums[i]
                else:
                    res[i] = 0
        return res

        
