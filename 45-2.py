from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        dp = [float('inf')] * n
        dp[0] = 0
        
        for i in range(1, n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[-1]
