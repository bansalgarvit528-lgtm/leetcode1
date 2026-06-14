class Solution:
    def pairSum(self, head):
        a = []

        while head:
            a.append(head.val)
            head = head.next

        m = 0

        for i in range(len(a)//2):
            s = a[i] + a[len(a)-1-i]

            if s > m:
                m = s

        return m