# TO-DO: Complete the selection_sort() function below 

#  arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
                
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]


    
    return arr
arr = [0, 3, 7, 1, 2, 8, 5, 4, 6, 9]
selection_sort(arr)
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_counter = -1
    while swap_counter != 0:
        swap_counter = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap_counter += 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr