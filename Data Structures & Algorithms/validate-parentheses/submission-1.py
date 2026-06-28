class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while i < len(s):

            if s[i]=="}" or s[i]=="]" or s[i]==")":
                if stack ==[]:
                    return False
                else:
                    if (stack[-1]=="{" and s[i]=="}") or (stack[-1]=="[" and s[i]=="]") or (stack[-1]=="(" and s[i]==")"):
                        stack.pop()
                    else:
                        return False
                i+=1
                print(stack)
            else:
                stack.append(s[i])
                i+=1
                print(stack)
        
        print(stack)
        
        if stack == []:
            return True
        else:
            return False
