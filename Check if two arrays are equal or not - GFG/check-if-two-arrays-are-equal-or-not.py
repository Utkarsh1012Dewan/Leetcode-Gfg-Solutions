#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        trackA = {}
        trackB = {}
        
        for i in A:
            trackA[i] = 1 + trackA.get(i,0)
        
        for i in B:
            trackB[i] = 1 + trackB.get(i,0)
        
        
        for i in trackA:
            if trackA[i] != trackB.get(i,0):
                return False
        
        
        return True
        
        
        
        
        #return: True or False
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends