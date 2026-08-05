class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)-1
        carry = 1
        while carry==1 and n>=0:
            if digits[n]+carry>9:
                digits[n]=0
                carry=1
            else:
                digits[n]+=carry
                carry=0
            n-=1
        if n<0 and carry!=0:
            ans = [1]+digits
            return ans
        else:
            return digits