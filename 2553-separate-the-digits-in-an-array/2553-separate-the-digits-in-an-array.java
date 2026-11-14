class Solution {
    public int[] separateDigits(int[] nums) {
        int digits=0;
        for(int num:nums){
            int temp=num;
            while(temp > 0){
                digits++;
                temp /= 10;
            }
        }
        int[] digit = new int[digits];
        int index = digits-1;
        for(int i=nums.length-1;i >= 0;i--){
            int num = nums[i];
            while(num >0){
                digit[index--] = num%10;
                num /= 10;
            }
        }
        return digit;
    }
}