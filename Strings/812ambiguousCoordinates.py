# class Solution:
def ambiguousCoordinates(S):
    """
    :type S: str
    :rtype: List[str]
    """
    output = []
    S = S[1: -1]
    i = 0
    while i < len(S) - 1:
        if S[:i + 1] == str(int(S[:i + 1])) and S[i + 1] == str(int(S[i + 1:])):
            output.append(("({}, {})").format(S[:i + 1], S[i + 1:]))

        i += 1
    i = 0
    while i < len(S) - 1:
        j = i + 1
        while j < len(S) - 1: #for decimal point on the x coordinate
            if S[:i +  1] == str(int(S[:i +  1])) and S[j + 1:] == str(int(S[j + 1:])):
                output.append(("({}.{}, {})").format(S[:i +  1], S[i + 1:j + 1], S[j + 1:]))
            j += 1
        p = i + 1
        while p < len(S) - 1: #for decimal on the y coordinate
            if S[:i +  1] == str(int(S[:i +  1])) and S[p + 1:] == str(int(S[p + 1:])):
                output.append(("({}, {}.{})").format(S[:i +  1], S[i + 1: p + 1], S[p + 1:]))
            p += 1
        i += 1
    # for i, coord in enumerate(output):
    #     index = coord.index(',')
    #     endIndex = coord.index(')')
    #     if len(coord[1:index]) > 1:
    #         if coord[1] == "0" and coord[2] != ".":
    #             del(output[i])
    #     elif len(coord[index + 2:endIndex]) > 1:
    #         if coord[index + 2] == "0" and coord[index + 3] != ".":
    #             del(output[i])

    return output

#print (ambiguousCoordinates("123"))
print (ambiguousCoordinates("(00011)"))
