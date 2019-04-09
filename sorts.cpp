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

//Merge Sort
// void mergeSort(vector<int> &array, int l, int r){
//     if(l < r){
//         int m = l+(r-1)/2;
//         mergeSort(array, l, m); 
//         mergeSort(array, m+1, r); 

//         //Merge
//         int i, j, k; 
//         int n1 = m - l + 1; 
//         int n2 =  r - m; 
    
//         /* create temp arrays */
//         vector<int> L, R;
//         L.resize(n1);
//         R.resize(n2); 
    
//         /* Copy data to temp arrays L[] and R[] */
//         for (i = 0; i < n1; i++) 
//             L[i] = array[l + i]; 
//         for (j = 0; j < n2; j++) 
//             R[j] = array[m + 1+ j]; 
    
//         /* Merge the temp arrays back into arr[l..r]*/
//         i = 0; // Initial index of first subarray 
//         j = 0; // Initial index of second subarray 
//         k = l; // Initial index of merged subarray 
//         while (i < n1 && j < n2) 
//         { 
//             if (L[i] <= R[j]) 
//             { 
//                 array[k] = L[i]; 
//                 i++; 
//             } 
//             else
//             { 
//                 array[k] = R[j]; 
//                 j++; 
//             } 
//             k++; 
//         } 
    
//         /* Copy the remaining elements of L[], if there 
//         are any */
//         while (i < n1) 
//         { 
//             array[k] = L[i]; 
//             i++; 
//             k++; 
//         } 
    
//         /* Copy the remaining elements of R[], if there 
//         are any */
//         while (j < n2) 
//         { 
//             array[k] = R[j]; 
//             j++; 
//             k++; 
//         } 
//     }
// }


// void Sort(vector<int> &array){

// }

int main(int argc, char* argv[]){
    vector<int> array = {10, 4, 25, 50, 75, 22, 21, 2, 6, 5, 3};

    // mergeSort(array, 0, array.size() - 1);
    cout << "num of exections(n = " << array.size() << "): " << insertionSort(array) << endl;
    for(int i = 0; i < array.size(); i++)
        cout << array[i] << endl;
    
    return 0;
}