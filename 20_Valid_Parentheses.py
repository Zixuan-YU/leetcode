class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            '}': '{',
            ']': '[',
            ')': '('

        }
        
        stack = []
        
        #print(dict)
        for i in s:
            
            if len(stack) > 0 and stack[-1] == dict.get(i, False):
                stack.pop(-1)
            else:
                stack.append(i)
        
        if len(stack) == 0:
            return True
        return False
