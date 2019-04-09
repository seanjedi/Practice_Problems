#include <iostream>
using namespace std;
int fib(int n){
    int fib0 = 0, fib1 = 1, fib = 0;
    for(int i = 1; i < n; i++){
        fib = fib1 + fib0;
        fib0 = fib1;
        fib1 = fib;
    }
    return fib;
}

int fibSlow(int n){
    if(n <= 0)
        return 0;
    if(n == 1)
        return 1;
    return fibSlow(n - 1) + fibSlow(n - 2);
}

int main(int argc, char* argv []){
    cout << fib(20) << endl;
    return 0;
}