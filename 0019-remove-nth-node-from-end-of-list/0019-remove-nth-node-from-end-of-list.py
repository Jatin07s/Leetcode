# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# BRUTE FORCE METHOD.....
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if head == None:
        #     return None
        # length = 0
        # temp = head
        # while temp != None:
        #     length += 1
        #     temp = temp.next
        # if length == n:
        #     new_head = head.next
        #     del head
        #     return new_head
        # pos = length - n
        # count = 1
        # temp = head
        # while count < pos:
        #     temp = temp.next
        #     count += 1
        # temp.next = temp.next.next    
        # return head


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head 
        fast=head
        for _ in range(n):  
            fast = fast.next
        if fast == None:
            return head.next    
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head    





