# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    for i in range(3):
        if arrA[i] < arrB[i]:
            merged_arr[i] = arrA[i]
        else: 
            merged_arr[i] = arrB[i]        
    
    return merged_arr
print(merge([1,4,5], [2,3,6]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


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

i = 0    

def recur_search(arr, num):
    global i
    if arr[i] == num:
        return True
    elif i < len(arr)-1:    
        i += 1   
        return recur_search(arr, num)   
    else: 
        return False 

print(recur_search([1,2,33,4,5], 5))