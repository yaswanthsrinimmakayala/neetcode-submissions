class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]*len(height)
        maxRight = [0]*len(height)
        maxLeft[0] = height[0]
        maxRight[-1]=height[-1]
        for i in range(1,len(height)):
            maxLeft[i] = max(maxLeft[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            maxRight[i] = max(maxRight[i+1],height[i])
        water = 0
        print(maxLeft)
        print(maxRight)
        for i in range(1,len(height)-1):
            water += max(0,min(maxRight[i+1],maxLeft[i-1])-height[i])
        return water
