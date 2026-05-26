class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeBrackets={')':'(','}':'{',']':'['}
        for c in s:
            if c in closeBrackets:
                
                if stack and stack[-1]==closeBrackets[c]:
                    stack.pop()
                   
                else:
                    return False

            else:
                stack.append(c)
                
        return True if not stack else False


        