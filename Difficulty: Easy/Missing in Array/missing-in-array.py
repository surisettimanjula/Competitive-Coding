#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        n = len(arr) + 1
        total_sum = n * (n + 1) / 2
        array_sum = sum(arr)
        return int(total_sum - array_sum)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(arr)
    print(s)

    print("~")
# } Driver Code Ends