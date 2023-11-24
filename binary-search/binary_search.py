import random
import time

def binary_search(array, target, start, end):
    if start < end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search(array, target, start, mid - 1)
        else:
            return binary_search(array, mid + 1, end, target)
    else:
        return -1

def linear_search(array, target):
    for i in array:
        if i == target:
            return i
    return -1


def main():
    # from 0 to 9999999 to perform binary/linear search on 
    a = []
    for i in range(1000000):
        a.append(i)

    # get 10000 random numbers to target with binary/linear search
    targets = []
    for i in range(10000):
        targets.append(random.randint(0, 999999))
    
    # binary search times
    bst = []
    for i in range(10000):
        start = time.perf_counter()
        binary_search(a, targets[i], 0, len(a) - 1)
        end = time.perf_counter()
        bst.append(end - start)

    # linear search times
    lst = []
    for i in range(10000):
        start = time.perf_counter()
        linear_search(a, targets[i])
        end = time.perf_counter()
        lst.append(end - start)

    print(f"Average Binary Search Time: {sum(bst) / len(bst)}")
    print(f"Average Linear Search Time: {sum(lst) / len(lst)}")

if __name__ == "__main__":
    main()