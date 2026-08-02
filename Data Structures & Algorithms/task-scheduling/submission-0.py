class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = {}
        for i in tasks:
            hm[i]  = hm.get(i,0)+1
        heap= []
        heapq.heapify(heap)
        for k,v in hm.items():
            heapq.heappush(heap,(-v,k))
        time = 0
        while heap:
            ls = []
            freq = n+1
            while freq>0 and heap:
                freq -=1
                v,k = heapq.heappop(heap)
                v = v+1
                time+=1
                if v!=0:
                    ls.append((v,k))
            if freq!=0 and ls:
                time+=freq
            if ls:
                for v,k in ls:
                    heapq.heappush(heap,(v,k))


        return time
