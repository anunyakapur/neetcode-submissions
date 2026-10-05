# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. check base case (empty list1 or list2)
        
        if not list1: # list1 is empty (if list 2 is empty too, this returns None)
            return list2

        elif not list2: # only list2 is empty
            return list1

        #2. assuming both are non-empty
        if list1.val <= list2.val:
            # list1.val adds to our new sorted list
            list1.next = self. mergeTwoLists(list1.next, list2)
            return list1
        else:
            # list2.val adds to our new sorted list
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2