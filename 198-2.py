from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1]

solution = Solution()

nums1 = [1, 1, 3, 3]
nums2 = [2, 9, 8, 3, 6]
print(solution.rob(nums1))  
print(solution.rob(nums2)) 
