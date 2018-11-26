# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
    countA = 0
    countB = 0

    if headA == None or headB == None:
	    return None

	Apointer = headA 
	Bpointer = headB

	while Apointer != Bpointer:
		if Apointer == None:
			Apointer = headB
		else:
			Apointer = Apointer.next
		if Bpointer == None:
			Bpointer = headA 
		else:
			Bpointer = Bpointer.next

	return Apointer
