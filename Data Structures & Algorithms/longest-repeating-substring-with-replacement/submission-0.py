class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = set(s)
        max_length = 0
        for c in charset:
            l = count = 0
            for r in range(len(s)):
                if s[r]==c:
                    count+=1
                
                while r-l+1 - count>k:
                    if s[l]==c:
                        count-=1
                    l = l+1
                max_length = max(r-l+1,max_length)
        return max_length
                