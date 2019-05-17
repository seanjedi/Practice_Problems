import time
import random

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

#O(N^2)
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] <= arr[j]:
                swap(arr, i, j)
    return arr

#O(N^2)
def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j
        swap(arr, i, min)
    return arr

#O(N^2)
def insertionSort(arr):
    sorted = []
    for i in range(len(arr)):
        if i is 0:
            sorted.append(arr[i])
        elif(sorted[i-1] <= arr[i]):
            sorted.append(arr[i])
        else:
            for j in range(len(sorted)):
                if sorted[j] > arr[i]:
                    sorted.insert(j, arr[i])
                    break
    return sorted

#Helper function for MergeSort
def merge(n1, n2):
    a = 0
    b = 0
    arr = []
    for i in range(len(n1) + len(n2)):
        if(b >= len(n2) or (a < len(n1) and n1[a] < n2[b])):
            arr.append(n1[a])
            a += 1
        else:
            arr.append(n2[b])
            b +=1
    return arr

#O(N log(N))
def mergeSort(arr):
    if len(arr) is 1:
        return arr
    middle = len(arr)//2
    left = arr[:middle]
    right = arr[middle:]
    result = merge(mergeSort(left), mergeSort(right))
    return result
    
def test1():
    array = [5,4,3,2,1,2,3,4,5, 8, 9, 6, 1, 10]
    print(mergeSort(array))
    print(bubbleSort(array))
    print(selectionSort(array))
    print(insertionSort(array))

def test2():
    array = []
    elements = 20
    for i in range(elements):
        array.append(int(random.random() * 1000000))
    print("array: ", array)
    print(mergeSort(array))
    print(bubbleSort(array))
    print(selectionSort(array))
    print(insertionSort(array))
    array.sort()
    print(array)

def timeTrial():
    array = []
    elements = 10000
    for i in range(elements):
        array.append(random.random() * 1000000)
    
    #Bubble Sort
    t1 = time.time()
    bubbleSort(array)
    t2 = time.time()
    print("this is how much time it takes to do bubbleSort: ", (t2-t1))

    #Selection Sort
    t1 = time.time()
    selectionSort(array)
    t2 = time.time()
    print("this is how much time it takes to do selectionSort: ", (t2-t1))

    #Insertion Sort
    t1 = time.time()
    insertionSort(array)
    t2 = time.time()
    print("this is how much time it takes to do insertionSort: ", (t2-t1))

    #Merge Sort
    t1 = time.time()
    mergeSort(array)
    t2 = time.time()
    print("this is how much time it takes to do mergeSort: ", (t2-t1))

    #Merge Sort
    t1 = time.time()
    array.sort()
    t2 = time.time()
    print("this is how much time it takes to do provided sort: ", (t2-t1))


test1()
test2()
timeTrial()