class Solution {
public:
    int minSteps(int n) {
        if(n==1){
            return 0;
        }else{
            for(int i=n-1;i>=2;i--){
                if(n%i==0){
                    return minSteps(i)+n/i;
                }
            }
        }
        return n;
    }
};