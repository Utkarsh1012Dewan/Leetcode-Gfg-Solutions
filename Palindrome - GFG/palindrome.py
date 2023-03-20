#User function Template for python3

class Solution:
	def is_palindrome(self, n):
	    
	    temp = 0
	    copy = n
	    
	    while n:
	        temp = (temp*10) + n%10
	        
	        n //=10
	        
	       
	    return "Yes" if temp == copy else "No"
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends