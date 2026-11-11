
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[nums[0], nums[0]]]  # [max ending here, min ending here]
        maxMult = nums[0]

        for i in range(1, len(nums)):
            prev = dp[i-1][0] * nums[i]
            prev2 = dp[i-1][1] * nums[i]
            curr = nums[i]

            dp.append([max(prev, prev2, curr), min(prev, prev2, curr)])
            maxMult = max(maxMult, dp[i][0])

        return maxMult
