class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int rightsum = 0, leftsum = 0, length = nums.size();
        vector<int> a;
        for(int i=0; i<length; i++){
            rightsum += nums[i];
        }
        for(int i=0; i<length; i++){
            leftsum += nums[i];
            a.push_back(abs(rightsum-leftsum));
            rightsum -= nums[i];
        }
        return a;
    }
};