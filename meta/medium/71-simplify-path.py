class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path = path.split("/")

        for part in path:
            if part == "..": 
                if stack:
                    stack.pop()
            
            elif part and part != ".":
                stack.append(part)
        


        return "/" + "/".join(stack)