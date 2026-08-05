class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        n = len(digits)-1
        for i in digits:
            ans = i*10**n+ans
            n-=1
        ans=ans+1
        ans_str = str(ans)
        result = []
        for i in ans_str:
            result.append(int(i))
        return result