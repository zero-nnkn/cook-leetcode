# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        cur_node = head
        next_node = head.next
        head.next = None
        while next_node:
            temp = next_node.next
            next_node.next = cur_node
            cur_node = next_node
            next_node = temp
        return cur_node
        
