class Solution {
public:
    bool isValid(string s) {
      std::stack<char> open;

        for (char c : s) {
            switch (c) {
                case '(':
                case '[':
                case '{':
                    open.push(c);
                    break;

                case ')':
                    if (open.empty() || open.top() != '(') return false;
                    open.pop();
                    break;
                case ']':
                    if (open.empty() || open.top() != '[') return false;
                    open.pop();
                    break;
                case '}':
                    if (open.empty() || open.top() != '{') return false;
                    open.pop();
                    break;
            }
        }

        return open.empty(); // Stack should be empty if valid
    }
};


 