//{ Driver Code Starts
// Initial template for C++
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    string removeChars(string string1, string string2) {
        string string3 = "";
        for(int i=0; i<string1.size(); i++){
            int status = 1;
            for(int j=0; j<string2.size(); j++){
                if(string1[i]==string2[j]){
                    status = 0;
                }
            }
            if(status){
                string3.push_back(string1[i]);
            }
        }
        return string3;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string string1,string2;
        cin >> string1; 
        cin >> string2;
        Solution ob;
        cout << ob.removeChars(string1,string2) << endl;
    }
    return 0;
}

// } Driver Code Ends