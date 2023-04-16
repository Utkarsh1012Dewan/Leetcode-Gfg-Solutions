#User function Template for python3

class Solution:
    def findMissing(self, arr, n):
        
        total = (n+1)/2 * (arr[0]+arr[n-1])
        
        for i in arr:
            total -= i
        
        
        return int(total)
        
        
        
        
        
        
        
        
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMissing(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends