class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+/-*"
        ans = 0
        if len(tokens)==1:
            return int(tokens[0])

        for i in range(len(tokens)):
            
            if tokens[i] in operators and len(stack)>0:
                first=int(stack.pop())
                second=int(stack.pop())
                if tokens[i] == '+':
                    ans = second+first
                if tokens[i] == '-':
                    ans = second-first
                if tokens[i] == '*':
                    ans = second*first
                if tokens[i] == '/':
                    ans = int(second / first)
                    
                stack.append(ans)
            else:
                stack.append(tokens[i])
    


        return ans 
