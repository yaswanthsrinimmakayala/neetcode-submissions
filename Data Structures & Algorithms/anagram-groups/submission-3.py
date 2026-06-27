class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for i in strs:
            freq = [0]*26
            for j in i:
               freq[ord(j)-ord('a')]+=1
            temp = tuple(freq)
            if temp in hm.keys():
                hm[temp].append(i)
            else:
                hm[temp] = [i]
        return list(hm.values())
        
        
        