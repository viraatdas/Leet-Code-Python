class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        dict = {}

    

        for i, p in enumerate(list2):
            if p in list1:
                if i+list1.index(p) in dict:
                    dict[i + list1.index(p)].append(p)
                else: 
                    dict[i + list1.index(p)] = [p]
        return dict[min(dict)]
        
        


