class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s)-1
        s = s.lower()
        while left<right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    return False
            if not s[left].isalnum():
                left+=1
            if not s[right].isalnum():
                right-=1
        return True