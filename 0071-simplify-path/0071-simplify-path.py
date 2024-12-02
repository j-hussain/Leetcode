class Solution:
    def simplifyPath(self, path: str) -> str:
        result = ""
        i = 0
        n = len(path)
        
        while i < n:
            while i < n and path[i] == '/':
                i += 1
            
            start = i
            while i < n and path[i] != '/':
                i += 1
            component = path[start:i]
            
            if component == "..":
                if result:
                    result = result[:result.rfind('/')]
            elif component and component != ".":
                result += "/" + component
        
        return result if result else "/"