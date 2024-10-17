# multiple assignment
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head  # Initialize prev to None, curr to head

        while curr:  # While there are still nodes to process
            curr.next, prev, curr = (
                prev,
                curr,
                curr.next,
            )  # Simultaneously update the pointers

        return prev  # Return the new head of the reversed list
