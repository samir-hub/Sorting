# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    
    a_index = 0
    b_index = 0
    i = 0

    while a_index < len(arrA) and b_index < len(arrB):
        if arrA[a_index] < arrB[b_index]:
            merged_arr[i] = arrA[a_index]
            a_index += 1
            i += 1
        elif arrA[a_index] >= arrB[b_index]: 
            merged_arr[i] = arrB[b_index]
            b_index += 1  
            i += 1  
        
    if a_index != len(arrA):
        merged_arr = merged_arr[:i] + arrA[a_index:]
    if b_index != len(arrB):
        merged_arr = merged_arr[:i] + arrB[b_index:]

    return merged_arr
#print(merge([5,7], [2,4]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) == 1: 
        return arr
    else:     
        left = merge_sort(arr[:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        print(left)
        print(right)
    return merge(left, right)
    

print(merge_sort([7,5,4,2,8,6,3,1]))

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

#print(recur_search([1,2,33,4,5], 5))
