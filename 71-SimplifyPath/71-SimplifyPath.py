# Last updated: 5/24/2025, 10:02:56 AM
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts=path.split('/')
        stack=[]
        for part in parts:
            if part=='' or part=='.':
                continue
            elif part=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/'+"/".join(stack)