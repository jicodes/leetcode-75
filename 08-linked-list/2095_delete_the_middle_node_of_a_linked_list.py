class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        # Edge case: If the list has only one node
        if not head or not head.next:
            return None

        slow = fast = head
        prev = None

        # Move slow one step and fast two steps
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Remove the middle node
        if prev:
            prev.next = slow.next

        return head  # Return the modified linked list
