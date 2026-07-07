class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT = {}
        for c in t:
            freqT[c] = freqT.get(c,0)+1
        need=len(freqT)
        result = ""
        k,m = -1,-1
        min_length = float("inf")
        for i in range(len(s)):
            count = 0
            freqS = {}
            for j in range(i,len(s)):
               freqS[s[j]] = 1+freqS.get(s[j],0)
               flag= True

               for c in freqT:
                if freqT[c]>freqS.get(c,0):
                    flag = False
                    break
               if flag and min_length>(j-i+1):
                min_length = j-i+1
                k = j
                m = i
                result = s[i:j+1]
               
        return result
                        