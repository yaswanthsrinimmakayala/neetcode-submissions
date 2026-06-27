class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [0]*len(nums)
        backward = [0]*len(nums)
        result = [0]*len(nums)
        forward[0] = nums[0]
        for i in range(1,len(nums)):
            forward[i]=nums[i]*forward[i-1]
        backward[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2,0,-1):
            backward[i] = nums[i]*backward[i+1]
        result[0] = backward[1]
        result[len(nums)-1] = forward[len(nums)-2]
        for i in range(1,len(nums)-1):
            result[i] = forward[i-1]*backward[i+1]
        return result
      