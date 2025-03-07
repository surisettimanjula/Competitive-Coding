#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        current_sum = 0
        start = 0
        for end in range(n):
            current_sum += arr[end]
            while current_sum > target and start <= end:
                current_sum -= arr[start]
                start += 1
            if current_sum == target:
                return [start + 1, end + 1]
        return [-1]

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends