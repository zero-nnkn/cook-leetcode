# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited_node = []
        # cur = head
        # while cur is not None:
        #     if cur in visited_node:
        #         return True
        #     visited_node.append(cur)
        #     cur = cur.next
        # return False 

        # Slow and Fast Pointers
        if head is None or head.next is None:
            return False

        slow, fast = head, head.next
        while slow is not None and fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
        