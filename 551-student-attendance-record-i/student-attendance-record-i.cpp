class Solution {
public:
    bool checkRecord(string s) {
        int count = 0;
        for(int i=0; i<s.size(); i++){
            if(s[i]=='A'){
                count++;
            }else if(s[i]=='L' && i > 0 && i < s.size()-1){
                if(s[i-1]=='L' && s[i+1]=='L'){
                    return false;
                }
            }
        }if(count > 1){
            return false;
        } 
        return true;
    }
};