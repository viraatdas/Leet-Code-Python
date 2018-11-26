def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    slow = head
    fast = head
    res = []
    while head:
        res.append(head.val)
    res = res[:n] + res[n+1:]
    node = ListNode(r[0])
    for i in range(1, len(res)):
        node.next = r[i]
        node = node.next

    return node
