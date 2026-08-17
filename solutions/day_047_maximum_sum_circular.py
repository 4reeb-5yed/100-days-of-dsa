def max_subarray_sum_circular(nums):
    total = sum(nums)
    max_kadane = kadane(nums)
    min_kadane = kadane([-x for x in nums])
    if min_kadane == -total:
        return max_kadane
    return max(max_kadane, total - min_kadane)

def kadane(nums):
    max_ending = max_so_far = nums[0]
    for num in nums[1:]:
        max_ending = max(num, max_ending + num)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far