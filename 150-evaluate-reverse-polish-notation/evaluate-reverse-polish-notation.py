def calculation( num2, num1, sign):

        if sign == "*":
            return   num2 * num1
        if sign == "-":
            return   num2 - num1
        if sign == "+":
            return   num2 + num1
        if sign == "/":
            return   int( num2 / num1 )
            
class Solution(object):
    def evalRPN(self, tokens):
        numStack = []
        valid = {"*", "+", "/", "-"}

        if len(tokens) == 1:
            return int(tokens[-1])

        curVal = 0
        for t in tokens:

            if t in valid:
                num1 = numStack.pop()
                num2 = numStack.pop()
                curVal = calculation(num2, num1, t)

                numStack.append(curVal)
            else:
                numStack.append(int(t))    

        return numStack.pop()          
