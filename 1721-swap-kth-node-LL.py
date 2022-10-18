# Leetcode 1721 - https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# Problem - You are given the head of a linked list, and an integer k. Return the head of the LL after 
# swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
# Solution - Adapted from https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1911996/Python-Simple-Solution-with-Explanation

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Naive: Convert LL to list, swap elements with slicing, convert back to LL
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l, r = head, head # Define two pointers both at the node head (which is null and points to first element) 
        # Traverse l to get to the k-1 element from the left due to 1 indexing of LL
        for i in range(k-1):
            l = l.next
        tail = l # Pointer l is now where we need it. Start tail node from here and traverse r along with it
        while tail.next:
            r, tail = r.next, tail.next # r will stay the same distance from tail...k-1 so it ends up k-1 from right
        l.val, r.val = r.val, l.val # Now swap r and l values in LL    
        return head
