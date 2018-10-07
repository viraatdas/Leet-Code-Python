# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def middleNode(head):
        """
        :type head: ListNode
        :rtype: ListNode
	"""
	
	count = 0
	temp_ListNode = head
	while (temp_ListNode != None):
		count+= 1
		temp_ListNode = temp_ListNode.next
	
	count = int(count/2)
		
	for _ in range(0, count):
		head = head.next
	
	return head
