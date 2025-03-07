#{ 
 # Driver Code Starts
# Initial Template for Python 3


# } Driver Code Ends

class Solution:
    def max_histogram_area(self, heights):
        stack = []
        max_area = 0
        index = 0

        while index < len(heights):
            if not stack or heights[stack[-1]] <= heights[index]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = (heights[top_of_stack] *
                        ((index - stack[-1] - 1) if stack else index))
                max_area = max(max_area, area)

        while stack:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            max_area = max(max_area, area)

        return max_area

    def maxArea(self, mat):
        if not mat or not mat[0]:
            return 0

        max_area = 0
        dp = [0] * len(mat[0])

        for row in mat:
            for i in range(len(row)):
                dp[i] = dp[i] + row[i] if row[i] == 1 else 0

            max_area = max(max_area, self.max_histogram_area(dp))

        return max_area

#{ 
 # Driver Code Starts.

# Driver Code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        R = int(input())
        C = int(input())
        mat = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            mat.append(line)
        print(Solution().maxArea(mat))
        print("~")

# } Driver Code Ends