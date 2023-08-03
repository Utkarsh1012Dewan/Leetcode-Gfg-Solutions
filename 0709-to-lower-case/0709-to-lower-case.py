class Solution:
    def toLowerCase(self, s: str) -> str:
        
        build  = []
        
        
        for i in s:
            build.append(i.lower())
            
            
        return "".join(build)
        