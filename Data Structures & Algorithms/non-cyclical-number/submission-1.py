class Solution:
    def isHappy(self, n: int) -> bool:
        num = [n]

        while n!=1:
            ans = 0
            for i in str(n):
                ans += int(i)**2
            if ans in num:
                break
            num.append(ans)
            n=ans
        print(n)
        if n==1:
            return True
        else:
            return False