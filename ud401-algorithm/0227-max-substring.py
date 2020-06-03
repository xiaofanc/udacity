# Given an integer array nums, find the contiguous subarray 
#(containing at least one number) which has the largest sum and return its sum.
"""
Let S(i) = the max sum obtained from a substring a1, a2, ... ai (first i characters of the input)
which includes ai

S(i) in terms of S(1), S(2).... S(i-1)
base case: S(0) = 0
recursive relation:
S(i) = ai + max(0, S(i-1)) -> only include ai or if we take the optimal substring for a1 through ai-1


"""

def maxsub(nums):
    dp, ans = 0, 0
    for i in range(len(nums)):
        dp = nums[i] + max(0, dp) # the max sum obtained from beginning to num[i] which includes num[i]
        ans = max(ans, dp)        # the max sum for any substring
    return ans

def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    max_sum = nums[0]
    for i in range(1, n):
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
        max_sum = max(nums[i], max_sum)
    return max_sum

print(maxsub([-2,1,-3,4,-1,2,1,-5,4]))