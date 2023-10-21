class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        priority_queue <pair <int, int> > q;
        q.push({nums[0], 0});
        int res = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            while (i - q.top().second > k) {
                q.pop();
            }

            int x = max(0, q.top().first) + nums[i];
            res = max(res, x);
            q.push({x, i});
        }
        
        return res;
    }
};