# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd_node, even_node = head, head.next
        first_even_node = even_node
        while even_node and even_node.next:
            odd_node.next, even_node.next = odd_node.next.next, even_node.next.next
            odd_node, even_node = odd_node.next, even_node.next 
        odd_node.next  = first_even_node
        return head
        
