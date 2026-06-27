class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using hashmap
        hm = {}
        hm1={}
        for i in strs:
            hm[i] = "".join(sorted(i))
            if hm[i] in hm1.keys():
                hm1[hm[i]].append(i)
            else:
                hm1[hm[i]] = [i]
        result = []
        for i in hm1.keys():
            result.append(hm1[i])
        return result
