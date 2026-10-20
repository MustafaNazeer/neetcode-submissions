class Solution {
public:
    bool isOperation(string s){
        if(s == "+" || s == "-" || s == "/" || s == "*"){
            return true;
        }
        return false;
    }
    int evalRPN(vector<string>& tokens) {
        stack <int> s = {};

        for(int i = 0; i < tokens.size(); i++){
            
            if(!isOperation(tokens[i])){
                s.push(stoi(tokens[i]));
                continue;
            } 
                
            
                if(tokens[i] == "+"){
                   int current = s.top();
                   s.pop();
                   int result = s.top() + current;
                   s.pop();
                   s.push(result);
                } else if(tokens[i] == "-"){
                    int current = s.top();
                   s.pop();
                   int result = s.top() - current;
                   s.pop();
                   s.push(result);
                } else if(tokens[i] == "/"){
                   int current = s.top();
                   s.pop();
                   int result = s.top() / current;
                   s.pop();
                   s.push(result);
                } else {
                    // tokens[i] == "*"
                   int current = s.top();
                   s.pop();
                   int result = s.top() * current;
                   s.pop();
                   s.push(result);
                }
            
        }
        return s.top();
    }
};
