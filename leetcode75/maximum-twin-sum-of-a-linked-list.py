# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    def pairSum(self, head: Optional[ListNode]) -> int:
        if head is None or head.next is None:
            return 0
        if head.next.next is None:
            return head.val + head.next.val
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        first_haft = head
        second_haft = self.reverseLinkedList(slow.next)
        max_sum = 0

        while second_haft:
            max_sum = max(max_sum, first_haft.val + second_haft.val)
            first_haft, second_haft = first_haft.next, second_haft.next

        return max_sum
