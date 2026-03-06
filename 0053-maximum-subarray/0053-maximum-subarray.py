class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = 0
        for n in nums:
            currSum+=n
            maxSum = max(maxSum,currSum)
            currSum = max(0,currSum)
        return maxSum