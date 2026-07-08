class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        max_value = max(nums[:k])
        result = []
        result.append(max_value)
        for i in range(k,len(nums)):
            if k!=2:
                if max_value==nums[i-k]:
                    max_value = max(nums[i-k+1:i+1]) 
                else:
                    max_value = max(max_value,nums[i])
            else:
                max_value = max(nums[i-k+1:i+1])
            result.append(max_value)   

        return result    

