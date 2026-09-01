class Solution {
    public int missingNumber(int[] nums) {
        int count=0;
        int sum=0;
        for(int i=0; i<nums.length; i++){
            sum=sum+nums[i];
        }
        for(int i=1; i<=nums.length; i++){
            count=count+i;
        }
        return count-sum;
        
    }
}