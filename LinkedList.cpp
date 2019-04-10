#include <iostream>
#include <vector> 

using namespace std;

//Single linked list practice
class lList{
    private:
    lList* next;
    int key;
    int value;

    public:
    lList(int newKey = 0, int newValue = 0){
        key = newKey;
        value = newValue;
        next = NULL;
    }

    ~lList(){
        while(this->getNext()){
            delete this->getNext();
        }
    }

    lList* getNext(){
        return this->next;
    }

    int getKey(){
        return this->key;
    }

    int getValue(){
        return this->value;
    }

    void setNext(lList* newItem){
        this->next = newItem;
    }

    int setKey(int newKey){
        this->key = newKey;
    }

    int setValue(int newValue){
        this->value = newValue;
    }

    void insert(int key, int value){
        lList* cur = this;
        while(cur->getNext()){
            cur = cur->getNext();
        }
        lList* newItem = new lList(key, value);
        cur->setNext(newItem);
    }

    int search(int key){
        lList* cur = this;
        while(cur->getKey() != key && cur->getNext()){
            cur = cur->getNext();
        }
        return ((cur->getKey() == key) ? cur->value : -1);
    }

    void printList(){
        lList* cur = this;
        while(cur){
            cout << "key: " <<  cur->getKey() <<" Value: " << cur->getValue() << endl;
            cur = cur->getNext();
        }
    }

    int deleteKey(int key);
    void deleteDups();
    int kFromLast(int n);
};
lList* head = new lList();

int lList::deleteKey(int key){
    lList* cur = this;
    lList* next = this->getNext();
    
    if(cur->getKey() == key){
        lList* temp = head;
        temp->setNext(NULL);
        delete temp;
        head = next;
        return 0;
    }

    while(next->getKey() != key && next->getNext()){
        cur = cur->getNext();
        next = cur->getNext();
    }
    if(next->getKey() == key){
        cur->setNext(next->getNext());
        next->setNext(NULL);
        delete next;
        return 0;
    }else{
        return -1;
    }
}

void lList::deleteDups(){
    lList* slow = this;
    lList* temp;
    lList* fast = slow ->getNext();
    while(slow){
        while(fast){
            if(slow->getValue() == fast->getValue()){
                temp = fast;
                fast = fast->getNext();
                head->deleteKey(temp->getKey());
            }else{
                fast = fast->getNext();
            }
        }
        if(slow->getNext())
            slow = slow->getNext();
        else break;
        if(slow->getNext())
            fast = slow->getNext();
    }
}

int lList::kFromLast(int n){
    lList* cur = head;
    lList* loc = head;
    int counter = -n;
    while(cur){
        if(counter < 0){
            counter++;
        }else{
            counter = loc->getKey();
            loc = loc->getNext(); 
        }
        cur = cur->getNext();
    }
    return counter;
}

int main(int argc, char* argv []){
    head ->insert(1,50);
    head ->insert(4,50);
    head ->insert(6,50);
    head->insert(2,10);
    head->insert(3,40);
    head->insert(6,10);
    head->insert(7,10);

    
    // cout << head->search(3) << endl;
    cout << head->kFromLast(10) << endl;
    // head->deleteDups();

    // head->printList();
    return 0;
}