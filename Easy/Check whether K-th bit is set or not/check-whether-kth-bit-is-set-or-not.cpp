//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution
{
    public:
    bool checkKthBit(int n, int k) {
        string numstr = bitset<32>(n).to_string();
        reverse(numstr.begin(), numstr.end());
        if(numstr[k] == '1' && n >= 1 && n <= 10000000000 && k >=0 && k<= 31){
            return true;}
        else
            return false;
    }
};


//{ Driver Code Starts.

// Driver Code
int main()
{
	int t;
	cin>>t;//taking testcases
	while(t--)
	{
	    long long n;
	    cin>>n;//input n
	    int k;
	    cin>>k;//bit number k
	    Solution obj;
	    if(obj.checkKthBit(n, k))
	        cout << "Yes" << endl;
	    else
	        cout << "No" << endl;
	}
	return 0;
}
// } Driver Code Ends