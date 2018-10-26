def spiralOrder(matrix):
    i = len(matrix)
    j = len(matrix[0])

    finList = []
    counter = 0
    while (counter != len(matrix) * len(matrix[0])):
        temp_i = 0
        temp_j = 0

        while temp_j < j:
            finList.append(matrix[temp_i][temp_j])
            temp_j += 1
            counter += 1
        
        temp_i + = 1
        while temp_i < i:
            finList.append(matrix[temp_i][temp_j])
            temp_i + = 1
            counter += 1
        
        temp_j += -1
        while temp_j >= 0:
            finList.append(matrix[temp_i][temp_j])
            temp_j += -1
            counter += 1
        i += - 1
        j += -1
        temp_i += -1
        while temp_i >=0:
            finList.append(matrix[temp_i][temp_j])
            temp_i += -1
            counter += 1
    
    return finList


        
