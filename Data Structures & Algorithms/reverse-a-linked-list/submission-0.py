# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        # We will loop until there are no more nodes to process
        while current:
            # 1. Store the next node so we don't lose it
            next_temp = current.next
            
            # 2. REVERSE: Make the current node point backwards to prev
            current.next = prev
            
            # 3. MOVE FORWARD: Shift prev and current one step down the list
            prev = current
            current = next_temp
            
        # The loop ends when 'current' is None. 'prev' is now the new head.
        return prev
        

        

        
        
        