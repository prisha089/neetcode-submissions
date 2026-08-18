class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens: 
            if token in operators: 
                second_num = stack.pop()
                first_num = stack.pop()
                if token == "+": 
                    result = first_num + second_num 
                elif token == "-": 
                    result = first_num - second_num 
                elif token == "*": 
                    result = first_num * second_num 
                else: 
                    result = int(first_num/second_num) 
                stack.append(result)
            else: 
                stack.append(int(token))
        return stack[0]
        