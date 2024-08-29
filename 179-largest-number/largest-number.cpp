class Solution {
public:
    string largestNumber(vector<int>& nums) {
        std::vector<std::string> strNums;
        for (int num : nums) {
            strNums.push_back(std::to_string(num));
        }
        std::sort(strNums.begin(), strNums.end(), [](const std::string& a, const std::string& b) {
            return a + b > b + a;
        });
        if (strNums[0] == "0") {
            return "0";
        }
        std::string result;
        for (const std::string& str : strNums) {
            result += str;
        }
        return result;
    }
};