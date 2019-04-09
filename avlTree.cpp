#include <iostream>
#include <string>

using namespace std;


class avlTree{
    private:
    int value;
    avlTree* left;
    avlTree* right;

    public:
    avlTree(int n){
        value = n;
        right = NULL;
        left = NULL;
    }

    ~avlTree(){
        cout << "Destroying node: " << this->getValue() << endl;
        if(this->getLeft())
            delete this->getLeft();
        if(this->getRight())
            delete this->getRight();
    }

    void setRight(int val){
        this->right = new avlTree(val);
    }

    void setLeft(int val){
        this->left = new avlTree(val);
    }

    void setValue(int val){
        this->value = val;
    }

    avlTree* getRight(){
        return this->right;
    }
    
    avlTree* getLeft(){
        return this->left;
    }

    int getValue(){
        return this->value;
    }

    //Rotations
    void rightRotate(){
        avlTree* middle = 
    }

    void leftRotate(){

    }


    //Check Levels Function
    int checkLevels(){
        avlTree* cur;
        int cases = 0;
        if(this->getLeft()){
            cases = this->getLeft()->checkLevels();
        }
        if(this->getRight()){
            cases = this->getRight()->checkLevels();
        }

        if(cases != 0){
            switch(cases):
                case 1:
                    this->leftRotate();
                    break;
                case 2:
                    this->rightRotate();
                    break;
                case 3:
                    this->leftRotate();
                    this->rightRotate();
                    break;
                case 4:
                    this->rightRotate();
                    this->leftRotate();
                    break;
        }

        if(this->getLeft() && !this->getRight()){
            cur = this->getLeft()
            if(cur->getLeft())
                return 1;
            if(cur->getRight){
                return 4;
            }
        }else if(this->getRight() && !this->getLeft()){
            cur = this->getRight()
            if(cur->getRight())
                return 2;
            if(cur->getLeft){
                return 3;
            }
        }
        return 0;
    }

    //Insert Function!
    void insert(int val);
};

avlTree *head;

void avlTree::insert(int val){
    avlTree* cur = this;
    if(this->getValue() < val){
        if(this->getRight())
            this->getRight()->insert(val);
        else
            this->setRight(val);
    }else{
        if(this->getLeft())
            this->getLeft()->insert(val);
        else
            this->setLeft(val);
    }
    
    //Check if uneven, start from head
    head->checkLevels();
};


int main(int argc, char* argv[]){
    head = new avlTree(20);
    head->insert(8);
    head->insert(22);
    head->insert(4);
    head->insert(12);
    head->insert(25);
    head->insert(10);
    head->insert(14);
    delete head;
    return 0;
}