#include <iostream>
#include <vector>

using namespace std;

#define MIN(a,b)((a)<(b)?(a):(b))

void swap(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
}

//Bubble Sort
int bubbleSort(vector<int> &array){
    int executions = 0;
    for(int i = 0; i < array.size(); i++){
        for(int j = 0; j < array.size(); j++){
            executions++;
            if(array[i] < array[j]){
                swap(array[i], array[j]);
            }
        }
    }
    return executions;
}

//Insertion Sort
int insertionSort(vector<int> &array){
    int valueInsert = 0, hole = 0, executions = 0;
    for(int i = 1; i < array.size(); i++){
        valueInsert = array[i];
        hole = i;
        while(valueInsert < array[hole - 1] && hole > 0){
            array[hole] = array[hole - 1];
            hole--;
            executions++;
        }
        executions++;
        array[hole] = valueInsert;
    }
    return executions;
}

//Selection Sort
int selectionSort(vector<int> &array){
    int executions = 0;
    for(int i = 0; i < array.size(); i++){
        int min = array[i], minLoc = i;
        for(int j = i; j < array.size(); j++){
            executions++;
            if(MIN(min, array[j]) != min){
                minLoc = j;
                min = array[j];
            }
        }
        swap(array[i], array[minLoc]);
    }
    return executions;
}

// Merge Sort
void merge(vector<int> &a, int low, int mid, int high){
    vector<int> b;
    b.resize(a.size());
    int l1 = low, l2 = mid+1, i;
    for(i = low; l1 <= mid && l2 <= high; i++){
        if(a[l1] < a[l2])
            b[i] = a[l1++];
        else
            b[i] = a[l2++];
    }
    while(l1 <= mid){
        b[i++] = a[l1++];
    }
    while(l2 <= high)
        b[i++] = a[l2++];
    for(int i = low; i <= high; i++)
        a[i] = b[i];
}

void mergeSort(vector<int> &a, int low, int high){
    if(low < high){
        int mid = (low + high) / 2;
        mergeSort(a, low, mid);
        mergeSort(a, mid+1, high);
        merge(a, low, mid, high);
    }
}


// void Sort(vector<int> &array){

// }

int main(int argc, char* argv[]){
    vector<int> array = {10, 4, 25, 50, 75, 22, 21, 2, 6, 5, 3};
    mergeSort(array, 0, array.size() - 1);
    // cout << "num of exections(n = " << array.size() << "): " << insertionSort(array) << endl;
    for(int i = 0; i < array.size(); i++)
        cout << array[i] << endl;
    
    return 0;
}