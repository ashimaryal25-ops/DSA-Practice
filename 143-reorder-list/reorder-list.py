# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        slow = head 
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None
        prev = None
        while cur != None:
            hold = cur
            cur = cur.next
            hold.next = prev
            prev = hold

        l1 = head
        l2 = prev
        
        while l2:
            tmp1 = l1.next
            tmp2 = l2.next

            l1.next = l2
            l2.next = tmp1
 
            l1 = tmp1
            l2 = tmp2

           




            





        