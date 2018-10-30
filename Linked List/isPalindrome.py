#using list
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        check = []
        while head:
            check.append(head.val)
            head = head.next

        if check == check[::-1]:
            return True
        return False

#O(1) space
