# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

my_array = [9,6,3,2,5,8,7,4,1]
print(selection_sort(my_array))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    successful = False
    while not successful:
        swaps = 0
        for i in range(0, len(arr) - 1):
            if arr[i+1] < arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps += 1
        if swaps == 0:
            successful = True    
    
    return arr

my_array = [9,6,3,2,5,8,7,4,1]
print(bubble_sort(my_array))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

