#include <iostream>
#include <string>
#include <cstring>
using namespace std;

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


int main(int argc, char* argv[]){
    parser();
    finder();
    return 0;
}