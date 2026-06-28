class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0 
        stack = []
        val = 0
        while i<len(tokens):
            if tokens[i]=="+" or tokens[i]=="-" or tokens[i]=="*" or tokens[i]=="/":
                a,b = stack.pop(), stack.pop()
                if tokens[i] == "+":
                    val = b+a
                elif tokens[i] == "-":
                    val = b-a
                elif tokens[i] == "*":
                    val = b*a
                elif tokens[i] == "/":
                    val = int(b/a)
                stack.append(val)
            else:
                stack.append(int(tokens[i]))
            i+=1
        return stack[-1]
