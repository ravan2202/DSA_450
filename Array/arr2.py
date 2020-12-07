#Find the maximum and minimum element in an array
def minmax(arr,low,high):
    arr_max=arr[low]
    arr_min=arr[low]

    # If there is only one element
    if low==high:
        arr_max=arr[low]
        arr_min=arr[low]
        return(arr_max,arr_min)
    
    # If there is only two element
    elif high==low+1:
        if arr[low]>arr[high]:
            arr_max=arr[low]
            arr_min=arr[high]
        else:
            arr_max=arr[high]
            arr_min=arr[low]
        return(arr_max,arr_min)

    
    # If there are more than 2 elements
    else:
        mid=((high+low)//2)
        arr_max1,arr_min1=minmax(arr,low,mid)
        arr_max2,arr_min2=minmax(arr,mid+1,high)    
    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))   

arr=[1,2,3,4,5]
arr_max, arr_min = minmax(arr,0,len(arr)-1)
print('Minimum element is ', arr_min)
print('nMaximum element is ', arr_max)


# we can also solve using sorting 
# using min max funtion 

#FOR ANY SUGGESTIONS YOU ARE WELCOME