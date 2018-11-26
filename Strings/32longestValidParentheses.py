class Solution:
        def longestValidParentheses(self, s):
            """
            :type s: str
            :rtype: int
            """
            # "()(()"
            # ")()())"

            counter = 0
            added = []
            for i in range(len(s)):
                if s[i] == '(':
                    for j in range(i, len(s)):
                        if s[j] == ')' and (j not in added):
                            counter += 2
                            added.append(j)
                            break
            return counter

pi = Solution()
