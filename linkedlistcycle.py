#linked list cycle (easy)

# tourtise and hare algorithm
# there is a fast pointer and a slow pointer if they meet each other before there is a exit (nul)
# there is a cycle

  def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        return False

