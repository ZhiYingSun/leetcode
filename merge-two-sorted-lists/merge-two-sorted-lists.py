# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # fist linked list question
        result = ListNode()
        head = result                       # pointer to the result linked list
        
        while l1 and l2 :                   # while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                result.next = l1            # the next node is the current node in l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next          
            result = result.next            # move to the next element in result
        
        if l1:
            result.next = l1
        if l2:
            result.next = l2
        
        return head.next                    # since first node in result is the default 0
            