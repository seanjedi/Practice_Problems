#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <unordered_map>
using namespace std;

void iterators(vector<int> example){
    for (auto i = example.begin(); i != example.end(); ++i) 
        cout << *i << " ";

    cout << "\nReverse" << endl;
    for (auto ir = example.rbegin(); ir != example.rend(); ++ir) 
        cout << *ir << " "; 
  
    cout << "\nOutput of crbegin and crend : "; 
    for (auto ir = example.crbegin(); ir != example.crend(); ++ir) 
        cout << *ir << " "; 
}

void capacity(vector<int> ex){
    cout << "Size : " << ex.size() << endl; 
    cout << "Capacity : " << ex.capacity() << endl; 
    cout << "Max_Size : " << ex.max_size() << endl;
    ex.resize(10, 0); 
    cout << "Size : " << ex.size()<<endl;
     for (auto i = ex.begin(); i != ex.end(); ++i) 
        cout << *i << " ";

    ex.shrink_to_fit(); 
    cout << "\nVector elements are: "; 
    for (auto it = ex.begin(); it != ex.end(); it++) 
        cout << *it << " "; 
}

void modifiers(vector<int> ex){
    // ex.assign(1,10);
    ex.erase(ex.begin() + 2);
    ex.insert(ex.begin(), 5); 
    for (auto it = ex.begin(); it != ex.end(); it++) 
        cout << *it << " ";
}

void sliding_door(vector<int> arr){
    set<int> quiz;
    for(int i = 0; i < arr.size(); i++){
        quiz.insert(arr[i]);
    }
    int median = quiz.size()/2;
    cout << median << endl;
    auto itr = quiz.begin();
    cout << *itr+median << endl;
    quiz.erase(*itr+median);
    for (itr = quiz.begin(); itr != quiz.end(); ++itr) 
    { 
        cout << '\t' << *itr; 
    } 
}

void longest_substring(vector<int> arr){

}

void sets(vector<int> arr){
    unordered_map<int, int> umap;
    for(int i = 0; i < arr.size(); i++)
        umap.insert(make_pair(arr[i], 1));
    umap[1]++;
    umap[10]++;
    cout << umap[10] << endl;
    if (umap.find(3) == umap.end()) 
        cout <<"not found" << endl; 
    else
        cout << "Found " << endl; 
    
}

int main()
{
    vector<int> arr = {1,2,3,4,5,6};
    vector<int> arr2 = {1,3,2,6,4,0};
    // iterators(arr);
    // capacity(arr);
    // modifiers(arr);
    // sliding_door(arr2);
    sets(arr2);
}