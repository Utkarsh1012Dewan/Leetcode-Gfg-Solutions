class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
    
    #optimzed 2-pointer
        index1 = len(s) - 1
        index2 = len(t) - 1
        
        
        while index1 >=0 or index2 >=0:
            i1= self.nextIndex(s,index1)
            i2= self.nextIndex(t,index2)
        
            if i1 < 0 and i2 < 0:
                return True
            if i1 < 0  or i2 < 0:
                return False
            if s[i1] !=t[i2]:
                return False
            index1 = i1 - 1
            index2 = i2 - 1
        
        return True
        
    
    def nextIndex(self,str,index):
        
        count  = 0
        while index >=0:
            if str[index] == "#":
                count +=1
            elif count > 0:
                count -=1
            else:
                break
        
            index-=1
        return index
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # Brute Force Stack Solution. Time and space = O(M+N)
        stackS = []
        stackT = []
        
        for i in s:
            if stackS and i == "#":
                stackS.pop()
                continue
            elif i == "#" and not stackS:
                continue
            stackS.append(i)
            
        for i in t:
            if stackT and i == "#":
                stackT.pop()
                continue
            elif i == "#" and not stackT:
                continue
            stackT.append(i)
        
        s1 = "".join(stackS) 
        t1 = "".join(stackT)
        
        return s1 == t1