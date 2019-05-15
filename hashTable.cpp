#include <iostream>
#include <vector>
#include <string>
#include <cstdlib> 
#include <ctime>

using namespace std;

int random;

class HashTable{
    private:
    vector<pair<int, int>> arrayList;
    int capacity;
    double loadFactor;
    pair<int, int> empty;

    public:
    HashTable(double load = 0.5, int initialSize = 1){
        loadFactor = load;
        capacity = 0;
        empty.first = -1;
        empty.second = -1;        
        arrayList.resize(initialSize, empty);
    }

    void reHash(){
        vector<pair<int, int>> newArray(arrayList);
        arrayList.clear();
        arrayList.resize(newArray.size()*2, empty);
        for(int i = 0; i < newArray.size(); i++){
            if(newArray[i].first != -1){
                insert(newArray[i].first, newArray[i].second);
            }
        }
    }

    bool insert(int key, int value){
        //resize the hashtable if needed
        
        if(capacity >= (arrayList.size() * loadFactor)){
            reHash();
        }
        int loc = hash(key) % arrayList.size();
        
        while(arrayList[loc].first != -1){
            loc++;
            if(loc == arrayList.size())
                loc = 0;
        }
        pair <int, int> temp (key,value);
        arrayList[loc] = temp;
        capacity++;
    }

    // float find(int key){
    //     int loc = hash(key) % arrayList.size();
    //     while(key != arrayList[loc].first){
    //         loc++;
    //         if(loc == arrayList.size())
    //             loc = 0;
    //         if(arrayList[loc].first == -1)
    //             return -1;
    //     }
    //     return arrayList[loc].second;
    // }

    float find(int key){
        int loc = hash(key) % arrayList.size();
        int result;
        while(true){
            if(key == arrayList[loc].first){
                result = arrayList[loc].second;
                break;
            }
            if(arrayList[loc].first == -1){
                result = -1;
                break;
            }
            loc++;
            if(loc == arrayList.size())
                loc = 0;
        }
        cout << "Find (key: " << key <<"): " << result << endl;
        return result;
    }

    int hash(int key){
        int hash = key%random;
        return hash;
    } 

    void printTable(){
        cout << "PrintTable: " << endl;
        for(int i = 0; i < arrayList.size(); i++){
            cout << "Key: " << arrayList[i].first << " Value: "  << arrayList[i].second << endl;
        }
    }

    void randomInsert(){
        int items = rand()%100 + 1;
        cout << items << endl;
        for(int i = 0; i < items; i++){
            insert(rand(),rand());
        }
    }
};

int main(){
    //Seed the RNG and set it
    srand(time(NULL));
    random = rand();
    //Create Hashtable and add to it
    HashTable table(1, 10);

    //Testing insertion
    table.insert(1,10);
    table.insert(2,20);
    table.insert(3,30);

    //Testing find
    table.find(1);
    table.find(2);
    table.find(3);
    table.find(10);

    //Testing Random Insert
    table.randomInsert();

    //Print out table
    table.printTable();

    //Testing find again
    table.find(1);
    table.find(2);
    table.find(3);
}