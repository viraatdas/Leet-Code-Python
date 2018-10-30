def findMedianSortedArrays(nums1, nums2):
    newNum = nums1 + nums2
    newNum.sort()

    length = len(newNum)
    if length % 2 == 0:
        return (newNum[length//2] + newNum[(length//2) + 1]) / 2

    else:
        return newNum[(length//2) + 1]
