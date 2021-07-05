    ## reason for 2 array is because I needed a way to perform binary search to find duplicate for log(n) time
    ## base array consists of sorted elements with no duplicates of size n
    ## dupicate array consists of a duplicate of size n+1
    ## by comparing the base_arr[index] with dup_arr[index] will tell me whether to go left or right for search
    
def binary_search(base_arr, dup_arr, start, end):
    if end >= start:
        mid = int((start + end) / 2)
        if dup_arr[mid] == dup_arr[mid+1]:
            return dup_arr[mid]
        elif base_arr[mid] == dup_arr[mid]:
            return binary_search(base_arr, dup_arr, mid + 1, end)
        elif base_arr[mid] != dup_arr[mid]:
            return binary_search(base_arr, dup_arr, start, mid - 1)


def main():
    base_arr1 = [1, 2, 3, 4, 10, 40, 50, 100]
    dup_arr1 = [1, 2, 3, 4, 10, 40, 50, 100, 100]

    base_arr2 = [1, 2, 3, 4, 10, 40, 50, 100]
    dup_arr2 = [1, 2, 3, 4, 10, 40, 50, 50, 100]

    base_arr3 = [1, 2, 3, 4, 10, 40, 50, 100]
    dup_arr3 = [1, 2, 2, 3, 4, 10, 40, 50, 100, 100]
    
    duplicate1 = binary_search(base_arr1, dup_arr1, 0, len(dup_arr1)-1)
    duplicate2 = binary_search(base_arr2, dup_arr2, 0, len(dup_arr2)-1)
    duplicate3 = binary_search(base_arr3, dup_arr3, 0, len(dup_arr3)-1)
    
    print(duplicate1)
    print(duplicate2)
    print(duplicate3)


main()