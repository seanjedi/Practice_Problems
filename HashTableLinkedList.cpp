#include <iostream>
#include <vector>
#include <string>
#include <cstdlib> 
#include <ctime>

using namespace std;

int random;

class dataNode{
    private:
    int key;
    int value;
    dataNode* next;

    public:
    dataNode(int keys, int values): key(keys), value(values), next(NULL){
    }
    ~dataNode(){
        while(this->getNext()){
            delete this->getNext();
        }
    }
    dataNode* getNext(){
        return this->next;
    }
    int getKey(){
        return this->key;
    }
    int getValue(){
        return this->value;
    }
    void setNext(dataNode* node){
        this->next = node;
    }
};

class HashTable{
    private:
    vector<dataNode*> arrayList;
    int capacity;
    double loadFactor;

    public:
    HashTable(int initialSize = 1, double load = 0.5): loadFactor(load), capacity(0){       
        arrayList.resize(initialSize, NULL);
    }

    ~HashTable(){
        //Make sure to delete each linked list!
        for(int i = 0; i < arrayList.size(); i++){
            if(arrayList[i] != NULL){
                delete arrayList[i];
            }
        }
    }

    void reHash(){
        vector<dataNode*> newArray(arrayList);
        arrayList.clear();
        arrayList.resize(newArray.size()*2, NULL);
        for(int i = 0; i < newArray.size(); i++){
            if(newArray[i] != NULL){
                dataNode* temp = newArray[i];
                while(temp){
                    insert(temp->getKey(), temp->getValue());
                    temp = temp->getNext();
                }
            }
        }
    }

    bool insert(int key, int value){
        //resize the hashtable if needed
        if(capacity > (arrayList.size() * loadFactor)){
            reHash();
        }
        dataNode* newItem = new dataNode(key, value);
        int loc = hash(key) % arrayList.size();
        
        if(arrayList[loc] == NULL){
            arrayList[loc] == newItem;
        }else{
            dataNode* temp = arrayList[loc];
            while(temp->getNext()){
                temp = temp->getNext();
            }
            temp->setNext(newItem);
        }
        capacity++;
    }

    float find(int key){
        int loc = hash(key) % arrayList.size();
        int result = -1;

        if(arrayList[loc] != NULL){
            dataNode* temp = arrayList[loc];
            while(temp){
                if(temp->getKey() == key){
                    result = temp->getValue();
                    cout << "Find (key: " << key <<"): " << result << endl;
                    break;
                }
                temp = temp->getNext();
            }
            if(result == -1)
                cout << "Find (key: NULL" << key <<"): NULL" << endl;
        }else{
            cout << "Find (key: NULL" << key <<"): NULL" << endl;
        }
        return result;
    }

    int hash(int key){
        int hash = key%random;
        return hash;
    } 

    void printTable(){
        cout << "PrintTable: " << endl;
        for(int i = 0; i < arrayList.size(); i++){
            if(arrayList[i] != NULL){
                dataNode* temp = arrayList[i];
                while(temp){
                    cout << "Key: " << temp->getKey() << " Value: "  << temp->getValue() << "Node->";
                    temp = temp->getNext();
                }
                cout << endl;
            }else{
                cout << "Key: NULL Value: NULL" << endl;
            }
        }
    }

    void randomInsert(){
        int items = rand()%100 + 1;
        cout << "Adding " << items << " Items!" << endl;
        for(int i = 0; i < items; i++){
            insert(rand(),rand());
        }
    }
};

int main(){
    //Seed the RNG and set it
    // srand(time(NULL));
    // random = rand();
    //Create Hashtable and add to it
    HashTable table;

    //Testing insertion
    table.insert(1,10);
    // table.insert(2,20);
    // table.insert(3,30);

    // //Testing find
    // table.find(1);
    // table.find(2);
    // table.find(3);
    // table.find(10);

    // //Testing Random Insert
    // table.randomInsert();

    // //Print out table
    // table.printTable();

    // //Testing find again
    // table.find(1);
    // table.find(2);
    // table.find(3);
}