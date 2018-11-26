def searchInsert(nums, target):
    index = len(nums) // 2 
    while not (target >= nums[target - 1] and target <= nums[target]): 
        if (nums[index] > target):
            index = (index + len(nums)) // 2
        else:
            index = index // 2
    return index
