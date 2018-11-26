def countSubstrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i):
            if s[j:i] == s[j:i][::-1]:
                count+=1

    return count
