import sys

def threeSumClosest(nums, target):
    nums.sort()

    if (len(nums) < 4):
        return sum(nums)

    result = nums[0] + nums[1] + nums[2]
    for i in range(0, len(nums) - 2):
        j = i + 1
        k = len(nums) - 1

        while j < k: 
            sumNum = nums[i] + nums[j] + nums[k]
            if (sumNum == target):
                return sumNum
            
            if (abs(target - sumNum) > abs(target - result)):
                result = sumNum

            if (sumNum < target):
                j = j + 1

            if (sumNum > target):
                k = k - 1
                
    return result 


print (threeSumClosest([-1,2,1,-4],1))
