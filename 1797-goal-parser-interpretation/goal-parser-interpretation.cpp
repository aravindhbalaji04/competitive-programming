class Solution {
public:
    string interpret(string command) {
        string result = "";
        for(int i=0; i<command.size(); ++i){
            if(command[i]=='(' && command[i+1]==')'){
                result.push_back('o');
            }else if (command[i]=='(' || command[i]==')'){
                continue;
            }else{
                result.push_back(command[i]);
            }
        }
        return result;
    }
};