class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")

        for p in paths:
            if p == "..":
                if stack:
                    stack.pop()
            elif p not in ["", "."]:
                stack.append(p)
        
        return "/" + "/".join(stack)