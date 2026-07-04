class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        i = 0
        ans = 0
        for j in range(len(s)):
            if s[j] in freq:
                while s[j] in freq:
                    freq.pop(s[i])
                    i+=1
                freq[s[j]]=1
            else:
                freq[s[j]] = freq.get(s[j],0)+1
                ans = max(ans,j-i+1)
        return ans