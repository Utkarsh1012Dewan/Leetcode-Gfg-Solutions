#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        track = {}
        
        for i in A:
            track[i] = 1 + track.get(i,0)
            
        for i in B:
            if i not in track:
                return False
            track[i] -=1
        
        
        for i in track:
            if track[i] != 0:
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