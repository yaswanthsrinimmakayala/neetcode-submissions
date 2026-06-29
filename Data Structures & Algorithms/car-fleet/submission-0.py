class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position,speed),reverse=True)
        time = [0]*len(position)
        for i in range(len(position)):
            time[i] = (target-pairs[i][0])/pairs[i][1]
        
        currTime = 0
        count = 0
        for i in time:
            if i > currTime:
                count+=1
                currTime = i
        return count
