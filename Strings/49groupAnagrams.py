class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dict = {}
        output = []
        for words in strs:
            if ''.join(sorted(words)) not in dict:
                dict[''.join(sorted(words))] = [words]
            else:
                dict[''.join(sorted(words))].append(words)

        for val in dict.values():
            output.append(val)
        return output
