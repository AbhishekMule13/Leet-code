# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = head
        
        while res and res.next:
            if res.val == res.next.val:
                res.next = res.next.next  # Skip the duplicate
            else:
                res = res.next  # Move forward
        
        return head