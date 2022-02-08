# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # first linked list question
        # maintain an unchanging reference to node ahead of the return node.
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
        
        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        if l1:
            result.next = l1
        if l2:
            result.next = l2
        
        return head.next                    # since first node in result is the default 0
            
# merge k lists
# compare one by one -> O(kN) brute force
# optimize comparison process with a heap -> O(N log k)
