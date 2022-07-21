class Solution(object):
    def reverseList(self, head):

        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = Node('1')
head.next = Node('2')
head.next.next = Node('3')
head.next.next.next = Node('4')
head.next.next.next.next = Node('5')
def reverseBetween(head, left, right):
    dummy = Node(0, head)
    leftprev, curr = dummy, head
    for i in range(left-1):
        leftprev, curr = curr, curr.next
    prev = None
    for i in range(right - left + 1):
        tempNext = curr.next
        curr.next = prev
        prev, curr = curr, tempNext
    leftprev.next.next = curr
    leftprev.next = prev
    return dummy.next
reverseBetween(head, 2, 4)