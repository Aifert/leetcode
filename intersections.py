# Definition for singly-linked list.

# THis one is saying if we traverse the linked list and we have two pointers,
# if they end up being the same at the end, then they must have intersected. if they don't then they never intersected
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA, pointerB = headA, headB

        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        return pointerA
