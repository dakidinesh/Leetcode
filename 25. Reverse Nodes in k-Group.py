"""Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        GroupPrev=dummy

        while True:
            a=self.kth(GroupPrev,k)
            if not a:
                break
            GroupNext=a.next

            #reverse
            prev,curr=a.next,GroupPrev.next

            while curr!=GroupNext:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp
            
            tmp=GroupPrev.next
            GroupPrev.next=a
            GroupPrev=tmp
        return dummy.next
        
    def kth(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
        