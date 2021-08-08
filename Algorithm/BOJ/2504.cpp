// [2504] 괄호의 값
// 스택
// 재귀
// 자료 구조

#include <iostream>
#include <stack>
#include <string>
#include <stdio.h>
using namespace std;

int main(){

    stack<char> st;
    stack<int> st2;
    
    char temp[33];
    scanf("%s",temp);
    string str = temp;
    
    for(int i =0; i<str.length(); i++){
        char ch = str[i];

        if(ch == '(' || ch=='['){
            st.push(ch);
            
        }
       
        else if (st.empty() == 0 && (ch==')' || ch==']')){
            if(ch==')' && st.top()== '('){
                st.pop();
                st.push('*');
                st2.push(2);
            }
            
            else if (ch==']' && st.top() == '['){
                st.pop();
                st.push('*');
                st2.push(3);
            }
            
            else if (st.top() == '*') {
                
                int num = 0;

                if(ch==')'){
                    while(st.empty() == 0 && st.top() == '*'){
                        num += (st2.top());
                        st.pop();
                        st2.pop();
                    }
                    
                    if(st.empty() == 0 && st.top() == '('){
                        st.pop();
                        st2.push((num*2));
                        st.push('*');
                    }
                    
                    else{
                        printf("%d", 0);
                        exit(0);
                    }
                    
                }
                
                else if(ch==']'){
                    while(st.empty() == 0 && st.top() == '*'){
                        num += (st2.top());
                        st.pop();
                        st2.pop();
                    }
                    
                    if(st.empty() == 0 && st.top() == '['){
                        st.pop();
                        st2.push((num*3));
                        st.push('*');
                    }
                    
                    else{
                        cout << 0 ;
                        exit(0);
                    }
                }
                
                else{
                    cout << 0 ;
                    exit(0);
                }
            }
        }
        
        else{
            cout << 0 ;
            exit(0);
        }
        
    }
    
    int result = 0;
    while(st2.empty() == 0 && st.empty() == 0){
        if(st.top() == '*'){
            result += st2.top();
            st2.pop();
            st.pop();
        }
        
        else{
            cout << 0 ;
            exit(0);
        }
    }
    
    if (st.empty() == 0){
        result = 0;
    }
    
    cout << result ;
    return 0;
}
