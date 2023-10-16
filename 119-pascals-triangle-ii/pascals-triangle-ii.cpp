class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<vector<int>> pascalTriangle(rowIndex + 1);
        pascalTriangle[0].push_back(1);
        for (int currentRow = 1; currentRow <= rowIndex; currentRow++) {
            pascalTriangle[currentRow].push_back(1);
            vector<int>& currentRowList = pascalTriangle[currentRow];
            vector<int>& previousRowList = pascalTriangle[currentRow - 1];
            for (int j = 1; j < previousRowList.size(); j++) {
                int sum = previousRowList[j] + previousRowList[j - 1];
                currentRowList.push_back(sum);
            }

                currentRowList.push_back(1);
        }

        return pascalTriangle[rowIndex];
    }
};