# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        window = []
        temp = head
        
        # Preload window
        for i in range(n+1):
            if temp is None:
                return head.next
            window.append(temp)
            temp = temp.next
        
        
        while temp is not None:
            window.pop(0)
            window.append(temp)
            temp = temp.next
            
        node = window[0]
        
        if node.next is None:
            return None
        
        node.next = node.next.next
        return head