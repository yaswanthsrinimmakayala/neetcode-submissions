class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## slow and fast pointers
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        nslow = 0 
        while slow!=nslow:
            slow = nums[slow]
            nslow = nums[nslow]
        return slow
