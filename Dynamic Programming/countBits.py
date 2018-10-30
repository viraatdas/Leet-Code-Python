def countBits(num):
    result = []
    for i in range(num+1, -1, -1):
        print (bin(i))
        result.append(bin(i).count('1'))
        
    return result
    
print (countBits(2))
