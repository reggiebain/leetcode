# This is a possible use case of the "tortoise and hare" or fast and slow pointers method (see this for a great explanation of 
# its use in detecting cycles in a LL https://www.geeksforgeeks.org/how-does-floyds-slow-and-fast-pointers-approach-work/). 
# The premise here is get a "fast" pointer that you iterate n steps in the LL ahead of the slow one. Then iterate them together 
# until fast hits the end of the LL (where it's next is null). Once you hit the end, slow.next is the guy you want to remove...so 
# set it's next to next.next, disconnecting the one you want to remove from the LL! There's a tricky edge case explained in the comments.

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head # Set up fast and slow pointers
        for i in range(n): # Iterate fast to get n ahead of slow
            fast = fast.next
        # Edge cases: (1) Single element to delete, (2) 2 elements where second element removed
        if not fast:
            return head.next # This can be the last value or null in edge case
        # Iterate fast pointer n forwards
        while fast.next: # Only check fast.next since slow.next will never go OOB.
            fast = fast.next # Fast is now n ahead of slow   
            slow = slow.next
        slow.next = slow.next.next
        return head
