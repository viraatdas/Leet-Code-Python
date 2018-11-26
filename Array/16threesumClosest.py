# from itertools import combinations
#
# class Solution:
#     def threeSumClosest(self, nums, target):
#         comb = list(combinations(nums, 3))
#         clSum = float('inf')
#         for tup in comb:
#             if sum(tup) - target < clSum - target:
#                 clSum = sum(tup)
#             elif target == sum(tup)
#                 return target
#         return clSum

class Solution:
    def threeSumClosest(self, nums, target):
        i = 0
        j = i + 1
        k = j + 1
        clSum = float('inf')
        while k < len(nums):
            temp_Sum = nums[i] + nums[j] + nums[k]
            if abs(temp_Sum - target) < abs(clSum - target):
                clSum = temp_Sum
            if k + 1 == len(nums):
                if j + 1 == len(nums) - 1:
                    if i + 1 == len(nums) - 2:
                        break
                    else:
                        i += 1
                else:
                    j += 1
            else:
                k += 1
        return clSum
