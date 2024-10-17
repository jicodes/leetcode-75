class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Edge case: If the list is empty or has only one node
        if not head or not head.next:
            return head

        odd = head  # Pointer for the last odd node
        even = head.next  # Pointer for the last even node
        even_head = even  # Keep track of the head of the even list

        # Rearrange the nodes
        while even and even.next:
            odd.next = even.next  # Connect odd nodes
            odd = odd.next  # Move to the next odd node
            even.next = odd.next  # Connect even nodes
            even = even.next  # Move to the next even node

        odd.next = even_head  # Connect odd list to even list

        return head  # Return the modified linked list
