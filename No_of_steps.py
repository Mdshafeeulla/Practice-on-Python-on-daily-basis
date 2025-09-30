class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        a = 1  # W(1)
        b = 2  # W(2)

        for i in range(3, n + 1):
            # Calculate W(i)
            current_ways = a + b

            # Slide the window for the next iteration:
            a = b  # W(i-2) is now the old W(i-1)
            b = current_ways  # W(i-1) is now the current W(i)

        # 'b' holds the final result, W(n)
        return current_ways

climb_solution = Solution()
result = climb_solution.climbStairs(4)
print(result)
