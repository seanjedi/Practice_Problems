#include <iostream>
#include <string>

using namespace std;

class biTree {
    private:
    //Data
    biTree* right;
    biTree* left;
    int value;

    public:
    //Constructor
    biTree(int n = 0){
        value = n;
        right = NULL;
        left = NULL;
    }

    //Destructor
    ~biTree(){
        if(left)
            delete left;
        if(right)
            delete right;
    }
    //left value
    biTree* getLeft(){
        return left;
    }
    //right value
    biTree* getRight(){
        return right;
    }
    //value
    int getValue(){
        return value;
    }

    //insert function
    void insert(int n){
        biTree* cur = this;
        if(cur == NULL){
            cur = new biTree(n);
        }else{
            if(n > cur->getValue()){
                if(cur->getRight())
                    cur->getRight()->insert(n);
                else
                    cur->right = new biTree(n);
            }else{
                if(cur->getLeft())
                    cur->getLeft()->insert(n);
                else
                    cur->left = new biTree(n);
            }
        }
    }

    //Inorder traversal
    void inOrder_print(){
        biTree* cur = this;
        if(cur->getLeft() != NULL){
            cur->getLeft()->inOrder_print();
        }
        cout << cur->getValue() << endl;
        if(cur->getRight() != NULL){
            cur->getRight()->inOrder_print();
        }
    }

    //Preorder traversal
    void preOrder_print(){
        biTree* cur = this;
        cout << cur->getValue() << endl;
        if(cur->getLeft() != NULL){
            cur->getLeft()->preOrder_print();
        }
        if(cur->getRight() != NULL){
            cur->getRight()->preOrder_print();
        }
    }

    //Postorder traversal
    void postOrder_print(){
        biTree* cur = this;
        if(cur->getLeft() != NULL){
            cur->getLeft()->postOrder_print();
        }
        if(cur->getRight() != NULL){
            cur->getRight()->postOrder_print();
        }
        cout << cur->getValue() << endl;
    }

     //Print Triangle traversal
    void printTriangle(int left = 0, int right = 0, bool flag = true){
        biTree* cur = this;
        if((left == 0 || right == 0 || !cur->getLeft() || !cur->getRight()) && flag){
            cout << cur->getValue() << endl;
        }
        if(cur->getLeft()){
            cur->getLeft()->printTriangle(left++, right);
        }
        if(cur->getRight()){
            right++;
            cur->getRight()->printTriangle(left, right++, false);
        }
        if((left == 0 || right == 0 || !cur->getLeft() || !cur->getRight()) && !flag)
            cout << cur->getValue() << endl;
        
    }

     //Level Print
    void printLevel(int level, int curLevel = 0){
        biTree* cur = this;
        if(curLevel == level)
            cout << cur->getValue() << endl;
        if(cur->getLeft())
            cur->getLeft()->printLevel(level, curLevel+1);
        if(cur->getRight())
            cur->getRight()->printLevel(level, curLevel+1);
    }
};

int main(int argc, char* argv[]){
    biTree *head = new biTree(20);
    head->insert(8);
    head->insert(22);
    head->insert(4);
    head->insert(12);
    head->insert(25);
    head->insert(10);
    head->insert(14);
    head->printTriangle();
    delete head;
    return 0;
}