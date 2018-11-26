def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    if len(nums) == 1:
        return True
    if nums[0] == 0:
        return False
    index = nums[0]

    while index < len(nums):
        maxNum = 0
        for i in range (index + 1, nums[index] + index + 1):
            if nums[i] > maxNum:
                maxNum = nums[i]
        if maxNum == 0:
            break
        index = maxNum

    if index >= len(nums) - 1:
        return True
    else:
        return False


pi = canJump([2,3,1,1,4])
print (pi)
