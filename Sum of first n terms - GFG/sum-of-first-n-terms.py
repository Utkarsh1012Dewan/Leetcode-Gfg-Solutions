#User function Template for python3

class Solution:
    def sumOfSeries(self,N):
        
        return ((N**2)*((N+1)**2))//4
            
        
        
            
         
            
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.sumOfSeries(N)) 
# } Driver Code Ends