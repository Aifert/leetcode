# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next


# an explanation will be
# when we make a dummy node, that means we have a dummy list so dummy -> .. -> ... -> ..., when we first create it it is still empty
# and then we make a pointer to point at the start of the dummy
# going through the sorted list provided and checking their values, we add it to the list
# the final condition is to check if any of the sorted list was longer than the other, if it is then we can just append it to the end of our newly
# created list since it is already sorted
# then just return our dummy node next so dummy -> 1 -> 2 etc, which will return 1 -> 2

# LEET CODE SOLUTION

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         fakehead = p = ListNode(-1)
#         while list1 or list2:
#             if list1 and list2:
#                 if list1.val > list2.val:
#                     p.next = list2
#                     p = p.next
#                     list2 = list2.next
#                 else:
#                     p.next = list1
#                     p = p.next
#                     list1 = list1.next
#             elif list1:
#                 p.next = list1
#                 p = p.next
#                 list1 = list1.next
#             else:
#                 p.next = list2
#                 p = p.next
#                 list2 = list2.next

#         return fakehead.next
