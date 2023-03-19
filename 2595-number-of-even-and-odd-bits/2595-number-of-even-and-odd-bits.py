class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        
        binary = int(format(n, 'b')) #convert the number to binary> The result is a string so convert it to integer
        even = odd  = 0
        i = 0 
        
        while binary > 0:
            copy = binary%10
            
            if i % 2 == 0 and copy == 1:
                even +=1
                
            elif i % 2 != 0 and copy == 1:
                odd +=1
                
            i+=1
            binary = binary//10
        
        return [even,odd]
        