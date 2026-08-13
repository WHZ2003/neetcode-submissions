class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = set(['+','-','*','/'])
        for c in tokens:
            if c in operations:
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                if c == '+':
                    stack.append(num2 + num1)
                elif c == '-':
                    stack.append(num2 - num1)
                elif c == '*':
                    stack.append(num2 * num1)
                else:
                    print(c)
                    stack.append(num2 / num1)
            else:
                stack.append(c)
            
        return int(stack.pop())
                

        