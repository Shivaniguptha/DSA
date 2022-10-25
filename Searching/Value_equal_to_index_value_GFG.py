# Given an array Arr of N positive integers. And we need to find the elements whose value is equal to that of its index value ( Consider 1-based indexing ).

#User function Template for python3
class Solution:

	def valueEqualToIndex(self,arr, n):
		# code here
		l=[]
		for i in range(0,n):
		    if arr[i]==i+1:
		        l.append(i+1)
		return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr, n)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1

# } Driver Code Ends
