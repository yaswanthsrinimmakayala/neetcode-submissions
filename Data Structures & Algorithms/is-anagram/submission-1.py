class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in hm.keys():
                hm[s[i]]+=1
            else:
                hm[s[i]] = 1

        for j in range(len(t)):
            if t[j] in hm.keys() and hm[t[j]]>0:
                hm[t[j]]-=1
            else:
                return False
        return True