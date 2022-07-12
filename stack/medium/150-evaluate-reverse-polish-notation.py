class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        
        ops = set()
        ops.add("+")
        ops.add("-")
        ops.add("*")
        ops.add("/")
        
        for c in tokens:
            if c in ops:
                num1 = numStack.pop()
                num2 = numStack.pop()
                
                if c == "+":
                    numStack.append(num2+num1)
                elif c == "-":
                    numStack.append(num2-num1)
                elif c == "*":
                    numStack.append(num2*num1)
                else:
                    numStack.append(int(num2/num1))
            
            else:
                numStack.append(int(c))
        
        
        return numStack.pop()