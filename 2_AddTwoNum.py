#coding=utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(-1)
        prev = ret
        carry = 0
        while l1 or l2:
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            value = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) / 10
            if prev.val == -1:
                prev.val = value
            else:
                prev.next = ListNode(value)
                prev = prev.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        if carry > 0:
            prev.next = ListNode(carry)
        return ret


if __name__ == '__main__':
    test = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(8)
    l2 = ListNode(0)
    print test.addTwoNumbers(l1, l2)

