def longestPalindrome(s):
    if (len(s) < 2):
        return s
    maxPalin = ""
    i = s[1]
    for i in range(1, len(s)):
        low = i - 1
        high = i
           while (low - 1 >= 0 or high < len(s) - 1):
                if (s[low] == s[high]):
                    maxPalin = s[low:high+1]

            
