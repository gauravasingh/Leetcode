class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for part in path.split('/'):
            if part == '' or part == '.':
                continue          # skip empty parts and '.'
            if part == '..':
                if stack:
                    stack.pop()  # go up one level if possible
            else:
                stack.append(part) # valid directory name
        
        return '/' + '/'.join(stack)
