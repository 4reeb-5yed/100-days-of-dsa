def rob_ii(nums):
    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

def rob_linear(nums):
    prev2, prev1 = 0, nums[0]
    for num in nums[1:]:
        prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1