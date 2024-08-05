# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        final=ListNode()
        man=final
        while head:
            p=head.val
            if p!=val:
                man.next=ListNode(p)
                man=man.next
            head=head.next
        return final.next