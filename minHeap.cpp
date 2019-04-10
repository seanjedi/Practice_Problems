#include <iostream>
#include <vector>

using namespace std;

class minHeap{
    private:
    int heapSize;
    vector<int> data;

    public:

    minHeap(int size = 10){
        if(size<=0)
            size = 1;
        heapSize = 0;
        data.resize(size);
    }

    int getParent(int i){
        return (i-1)/2;
    }

    int getLeft(int i){
        return(i*2) + 1;
    }

    int getRight(int i){
        return (i*2) + 2;
    }

    void insert(int value){
        //If head needs to be filled, fill head, otherwise find where to insert and bubble up!
        if(heapSize == 0){
            data[0] = value;
        }else{
            if(heapSize == data.capacity()){
                data.resize(data.capacity()*2);
            }
            int i = heapSize;
            data[heapSize] = value;
            while(i != 0 && data[getParent(i)] > data[i]){
                swap(data[i], data[getParent(i)]);
                i = getParent(i);
            }
        }
        heapSize++;
    }

    int extractMin(){
        int min = data[0];
        if(heapSize <= 0 ){
            return -1;
        }
        if(heapSize == 1){
            heapSize--;
            return min;
        }
        data[0] = data[heapSize-1]; 
        heapSize--; 
        minHeapify();
        return min;
    }

    void minHeapify(int i = 0){
        int right = getRight(i);
        int left  = getLeft(i);

        int smallest = i; 
        if (left < heapSize && data[left] < data[i]) 
            smallest = left; 
        if (right < heapSize && data[right] < data[smallest]) 
            smallest = right; 
        if (smallest != i) 
        { 
            swap(data[i], data[smallest]); 
            minHeapify(smallest); 
        } 
    }
};

int main(int argc, char* argv[]){
    minHeap head(0);
    head.insert(10);
    head.insert(30);
    head.insert(25);
    head.insert(40);
    cout << head.extractMin() << endl;
    cout << head.extractMin() << endl;
    cout << head.extractMin() << endl;
    cout << head.extractMin() << endl;
    cout << head.extractMin() << endl;
    cout << head.extractMin() << endl;
    
}