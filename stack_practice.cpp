#include <iostream>

using namespace std;

//A node that will store interger values and the next and previous pointers
//Could change to another type or use a template to store different data types
class node{
    private:
    int value;
    node* next;
    node* prev;

    public:
    node(int data, node* previous = NULL){
        next = NULL;
        prev = previous;
        value = data;
    }
    node* getNext(){
        return this->next;
    }

    void setNext(node* node){
        this->next = node;
    }

    node* getPrev(){
        return this->prev;
    }

    void setPrev(node* node){
        this->prev = node;
    }

    int getData(){
        return this->value;
    }

    void setData(int data){
        this->value = data;
    }
};

//Double linked list implementation
//Could implement normal insert and remove functions
//But I will focus on the ones we need for the stack
class double_linked_list{
    private:
    node* head;
    node* tail;

    public:
    //Initialize head and tail to NULL
    double_linked_list(){
        head = NULL;
        tail = NULL;
    }

    //When deleted, needs to cleanup the nodes we allocated or else have a memory leak
    //This will be O(N)
    ~double_linked_list(){
        //start from the head
        node* cur = this->head;
        while(cur != NULL){
            //If the current node isn't the head, get rid of the previous node,
            //This will also take care of the head and allow the current pointer to move forward
            if(cur != this->head){
                delete cur->getPrev();
            }
            //If current pointer is the tail, delete the cur pointer/tail and make cur NULL to exit while loop
            //Else get the next node
            if(cur == this->tail){
                delete cur;
                cur = NULL;
            }else{
                cur = cur->getNext();
            }
        }
    }

    //Function to insert at the back of the linked list and updates tail pointer
    //This will be O(1)
    void insert_tail(int data){
        if(head == NULL){
            this->head = new node(data);
            this->tail = head;
        }else{
            node* newTail = new node(data, this->tail);
            tail->setNext(newTail);
            this->tail = newTail;
        }
    }

    //Function to get data at the tail pointer
    //This will be O(1)
    int get_tail_data(){
        if(tail == NULL){
            // Cannot get the tail! There is no data yet!
            throw -1;
        }
        return this->tail->getData();
    }

    //Function to remove the tail
    //This will be O(1)
    void remove_tail(){
        //If list is empty, return error
        if(head == NULL){
            // throw "The List is Empty!";
            throw -1;
        }else{
            //if tail and head are the same, then delete the head node and set head to NULL
            if(tail == head){
                delete this->head;
                this->head = NULL;
                this->tail = NULL;
            }
            else{
                this->tail = this->tail->getPrev();
                delete this->tail->getNext();
            }
        }
    }
};

//Stack with double linked list implementation
class stack{
    private:
    double_linked_list* dList;

    public:
    stack(){
        dList = new double_linked_list();
    }

    ~stack(){
        delete dList;
    }

    void push_back(int data){
        dList->insert_tail(data);
    }

    int top(){
        try {
            cout << dList->get_tail_data() << endl;
        } catch (int msg) {
            cerr << "Can't use top!\nThere is no data in Stack yet!" << endl;
        }
    }

    int pop(){
        try {
            dList->remove_tail();
        } catch (int msg) {
            cerr << "Can't use pop!\nThere is no data in Stack yet!" << endl;
        }
    }

};

int main(){
    //Some testing
    cout << "<--- Stack 1 Tests -->" << endl;
    stack* Stack_ptr = new stack();
    Stack_ptr->top();
    Stack_ptr->pop();
    Stack_ptr->push_back(1);
    Stack_ptr->top();
    Stack_ptr->push_back(2);
    Stack_ptr->top();
    Stack_ptr->push_back(3);
    Stack_ptr->top();
    delete Stack_ptr;

    //More testing
    cout << "<--- Stack 2 Tests -->" << endl;
    stack Stack;
    Stack.push_back(1);
    Stack.push_back(2);
    Stack.push_back(3);
    Stack.top();
    Stack.pop();
    Stack.top();
    Stack.pop();
    Stack.top();
    Stack.pop();
    Stack.top();
    Stack.pop();
    Stack.top(); 

}