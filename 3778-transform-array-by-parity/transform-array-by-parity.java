import java.util.*;

class Solution {
    public int[] transformArray(int[] nums) {
        ArrayList<Integer> arr = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0) {
                arr.add(0);
            } else {
                arr.add(1);
            }
        }

        Collections.sort(arr);

        int[] result = new int[arr.size()];

        for (int i = 0; i < arr.size(); i++) {
            result[i] = arr.get(i);
        }

        return result;
    }
}