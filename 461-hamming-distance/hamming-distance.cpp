class Solution {
public:
    int hammingDistance(int x, int y) {
        int ans=0;
        while(x || y){
            int mask=x&1;
            int mask2=y&1;
            if(mask!=mask2){
                ans++;
            }
            x>>=1;
            y>>=1;
        }
        return ans;
    }
};