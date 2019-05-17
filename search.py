import random
import time
import math

elements = 1000000
arr = []
t1 = time.time()
for i in range(elements):
    arr.append(random.randint(-elements, elements))
t2 = time.time()
print("took this long to make", t2-t1)

#linear search O(N)
def linearSeach(arr, n):
    for i in range(len(arr)):
        if(arr[i] is n):
            return True
    return False

#binary search O(log N)
def binarySearch(arr, n):
    middle = len(arr)//2
    if(arr[middle] is n):
        return True
    if(middle is 0):
        return False
    if(arr[middle] >= n):
        array = arr[:middle]
    else:
        array = arr[middle:]
    return(binarySearch(array, n))


find = random.randint(-elements - 10, elements + 10)
arr.insert(random.randint(0,elements-1) , find)
# arr.append(find)
# arr.insert(len(arr)//2, find)

arr.sort()

t1 = time.time()
print(linearSeach(arr, find))
t2 = time.time()
print("linear search took this long: ", t2-t1)

t1 = time.time()
print(binarySearch(arr, find))
t2 = time.time()
print("binary search took this long: ", t2-t1)