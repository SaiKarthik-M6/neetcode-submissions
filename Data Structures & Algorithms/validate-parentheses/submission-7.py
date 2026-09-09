class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for char in s: 
            if char == ('(') or char == ('{') or char == ('['):
                stack.append(char)
                continue
            
            elif char == (')'):
                if len(stack) != 0 and stack[-1] == '(' :
                    stack.pop()
                    continue
                return False

            elif char == (']'):
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                    continue
                return False

            elif char == ('}'):
                if len(stack) != 0 and stack[-1] == '{':
                    stack.pop()
                    continue
                return False

        if stack == []:
            return True
        
        return False



                