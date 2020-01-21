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
        print(arr)

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
                arr[i+1], arr[i] = arr[i], arr[i+1]
                swaps += 1
                print(arr)
        if swaps == 0:
            successful = True    
    
    return arr

my_array = [9,6,3,2,5,8,7,4,1]
print(bubble_sort(my_array))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr




    if arrA[0] < arrB[0]:
        merged_arr[0] = arrA[0]      
        merged_arr[1] = arrB[0] 
    else: 
        merged_arr[1] = arrA[0]      
        merged_arr[0] = arrB[0]

    if arrA[1] < arrB[1]:
        merged_arr[2] = arrA[1]      
        merged_arr[3] = arrB[1] 
    else: 
        merged_arr[3] = arrA[1]      
        merged_arr[2] = arrB[1]  

    if arrA[2] < arrB[2]:
        merged_arr[4] = arrA[2]      
        merged_arr[5] = arrB[2] 
    else: 
        merged_arr[5] = arrA[2]  
        merged_arr[4] = arrB[2]

    if arrA[3] < arrB[3]:
        merged_arr[6] = arrA[3]      
        merged_arr[7] = arrB[3] 
    else: 
        merged_arr[7] = arrA[3] 
        merged_arr[6] = arrB[3] 

        for i in range(len(arrA)):
        if arrA[i] < arrB[i]:
            merged_arr[(i*2)] = arrA[i]      
            merged_arr[i*2+1] = arrB[i] 
        else: 
            merged_arr[(i*2)+1] = arrA[i]      
            merged_arr[i*2] = arrB[i]  