class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = 0
        maxRight = 0
        water=0
        for i in range(len(height)):
            k,j=i-1,i+1
            while k>=0:
                maxLeft = max(maxLeft,height[k])
                k-=1
            while j<=len(height)-1:
                maxRight = max(maxRight,height[j])
                j+=1
            water += max((min(maxLeft,maxRight)-height[i]),0)
            maxLeft = 0
            maxRight = 0
        return water