class Solution {
    public ListNode rotateRight(ListNode head, int k) {

        if (head == null || head.next == null)
            return head;

        int n = 1;
        ListNode temp = head;

        while (temp.next != null) {
            temp = temp.next;
            n++;
        }

        temp.next = head;
        k = k % n;

        int steps = n - k;

        while (steps-- > 0)
            temp = temp.next;

        head = temp.next;
        temp.next = null;

        return head;
    }
}