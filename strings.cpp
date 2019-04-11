#include <iostream>
#include <string>
#include <cstring>
#include <stack>
#include <vector>
using namespace std;



//Auxiliary Functions
void sort(string& str){
    for(int i = 0; i < str.length(); i ++){
        for(int j = 0; j < str.length(); j++){
            if((int)str[i] < (int)str[j])
            swap(str[i], str[j]);
        }
    }
}

int map(char c, vector<char>& table){
    int i = (int)c;
    int loc = i%27;

    table[loc]++;
    return loc;
}


//General Practice
void parser(){
    string message = "This is a message to be broken!";
    char* cstr = new char[message.length() + 1];
    strcpy(cstr, message.c_str());
    char* pch = strtok(cstr, " ");
    while(pch != NULL){
        cout << pch << endl;
        pch = strtok(NULL, " ");
    } 
}

void finder(){
    string message = "Start: abcdefg message: gfbasc";
    size_t start = message.find("Start:");
    size_t end = message.find("message:");
    
    string string1 = message.substr(start + sizeof("Start"), end - sizeof("Start:"));
    string string2 = message.substr(end + sizeof("message"));
    cout << string1 << endl << string2 << endl;
}

int mapNoCollision(char c, vector<char>& table){
    int i = (int)c;
    int loc = i%27;
    if(table[loc] == 0){
        table[loc]++;
        return loc;
    }
    else
        return -1;
}


//Cracking the coding interview!
void question1(){
     string message = "aabcdefg";
     int loc;  
     bool flag = true;
     vector<char> table(27, 0);
     for(int i = 0; i < message.length(); i++){
         if(mapNoCollision(message[i], table) == -1){
            cout << "There was a duplicate!" << endl;
            flag = false;
         }
     }
     if(flag)
        cout << "All unique!" << endl;
}


void question2(){
    string message1 = "";
    string message2 = "";
    bool flag = true;
    if(message1.length() != message2.length())
        flag = false;
    
    if(flag){
        sort(message1);
        sort(message2);
        for(int i = 0; i < message1.length(); i++){
            if(message1[i] != message2[i]){
                flag = false;
                break;
            }
        }
    }
    if(flag)
        cout << "Its a permutation!"<< endl;
    else
        cout << "Not a permutation!" << endl;

}

void question3(){
    int n;
    string message = "Mr John Smith    ";
    string result;
    char* cstr = new char[message.length() + 1];
    strcpy(cstr, message.c_str());
    char* pch = strtok(cstr, " ");
    result.append(pch);
    while(pch != NULL){
        pch = strtok(NULL, " ");
        if(pch != NULL){
            result.append("%20");
            result.append(pch);
        }
    }
    cout << result << endl;
}

void Reversal(){
    string message = "Hi my name is Sean";
    string result;

    for(int i = message.length()-1; i >= 0; i--){
        result += message[i];
    }
    cout << result << endl;
    
}



int main(int argc, char* argv[]){
    // parser();
    // finder();
    // question1();
    // question2();
    // question3();
    // Reversal();
    return 0;
}