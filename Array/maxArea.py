def maxArea(height):
    i = 0
    j = len(height) - 1
    max_num = 0

    while(j != i):
        if (height[i] < height[j]):
            max_num = max((j - i) * (height[i]), max_num)
            i = i + 1
        else:
            max_num = max((j - i) * (height[j]), max_num)
            j = j - 1

    return max_num



print (maxArea([1,8,6,2,5,4,8,3,7]))
