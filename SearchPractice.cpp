#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

bool binarySearch(int* arr, int arrSize, int n){
    int high = arrSize;
    int low = 0;
    int loc = 0;
    while(loc >= 0 && loc < arrSize){
        loc = low + ( high - low ) / 2;
        
        if(arr[loc] == n)
            return true;
        
        if(arr[loc] < n)
            low = loc+1;
        
        else if(arr[loc] > n)
            high = loc - 1;
    }
    return false;
}

int AddsUp(int* arr, int arrSize, int n){
    int result = 0;
    for(int i = 0; i < 6; i++){
        int checkNum = n - arr[i];
        if(binarySearch(arr, arrSize, checkNum))
            result++;
    }
    return result;
}

bool hasCompliment(vector<int> arr, int n){
    unordered_set<int> compare;

    for(int i = 0; i < arr.size(); i++){
        compare.insert(n - arr[i]);
        if(compare.find(arr[i]) != compare.end()){
            return true;
        }
    }
    return false;
}

int main(int argv, char* argc[]){

    int arr[] = {1,2,3,4,5,6};
    vector<int> arr2 = {1,2,3,4,5,6};
    int arrSize = sizeof(arr) / sizeof(arr[0]);
    cout << hasCompliment(arr2, 200) << endl;

    return 0;
}