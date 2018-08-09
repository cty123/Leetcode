class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = self.getNodeVal(l1)
        num2 = self.getNodeVal(l2)
        sum = num1 + num2

        quo = sum // 10
        ret = ListNode(sum % 10)
        node = ret

        while quo != 0:
            node.next = ListNode(quo % 10)
            node = node.next
            quo = quo // 10
        return ret

    def getNodeVal(self, l):
        num = 0
        count = 0
        node = l
        while node is not None:
            num += node.val * 10 ** count
            count = count + 1
            node = node.next
        return num

s = Solution()
ls = ListNode(2)
print(s.addTwoNumbers(ls, ls))