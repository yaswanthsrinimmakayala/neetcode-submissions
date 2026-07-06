class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}

        for i in range(len(s1)):
            freq1[s1[i]] = 1 + freq1.get(s1[i],0)
        n = len(freq1)
        
        for i in range(len(s2)):
            freq2, cur = {}, 0
            for j in range(i, len(s2)):
                freq2[s2[j]] = 1 + freq2.get(s2[j],0)
                if freq1.get(s2[j],0)<freq2[s2[j]]:
                    break
                if freq1.get(s2[j],0)==freq2[s2[j]]:
                    cur+=1
                if cur==n:
                    return True
        return False