#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        
        count = 0
        copy = N
        
        while copy:
            r = copy%10
            
            if r != 0 and N%r == 0:
                count +=1
            copy //=10
        return count
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends