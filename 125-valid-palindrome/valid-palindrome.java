class Solution {
    public boolean isPalindrome(String s) {

        s = s.toLowerCase();
        String str = "";

        // Keep only letters and numbers
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetterOrDigit(s.charAt(i))) {
                str = str + s.charAt(i);
            }
        }

        int left = 0;
        int right = str.length() - 1;

        // Check palindrome
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}