class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        i = 0 
        while i<len(temperatures):
            while stack and temperatures[i]>stack[-1][0]:
                temp,indx = stack.pop()
                result[indx] = i-indx
            stack.append([temperatures[i],i])
            i+=1
        return result