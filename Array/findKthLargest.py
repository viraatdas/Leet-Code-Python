def findKthLargest(nums, k):
    nums.sort()
    print (nums)
    return (nums[len(nums) - k])

