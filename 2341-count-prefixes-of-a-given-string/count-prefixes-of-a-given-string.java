class Solution {
    public int countPrefixes(String[] words, String s) {
        int c=0;
        for(String s1:words){
          if(s.startsWith(s1))
            c++;
          }
         return c;
       }
   }