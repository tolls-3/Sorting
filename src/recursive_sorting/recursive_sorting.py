arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    merged_arr = []
    i = 0
    j = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1

    if i == len(arrA):
        merged_arr.extend(arrB[j:])
    else:
        merged_arr.extend(arrA[i:])        
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        high = len(arr)
        low = 0
        mid = round((high + low) / 2)

        leftArr = arr[low:mid]
        rightArr = arr[mid:]

        return merge(merge_sort(leftArr), merge_sort(rightArr))
print(merge_sort(arr1))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
