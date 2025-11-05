def binary(arr,targetVal):
    left=0
    right = len(arr) -1 
    while left<=right:
        mid= (left+right) //2
        if arr[mid] == targetVal:
            return mid
        if arr[mid] <targetVal:
            left = mid+1
        else:
            right = mid -1
    return -1

mi_Array = [1,3,5,7,9,11,13,15,17,19]
myTarget = 5
result = binary(mi_Array,myTarget)
if result != -1:

