#Find the "Kth" max and min element of an array 
def kthMinMax(arr,length,k):
    arr.sort()
    kthMin = arr[k-1]
    kthMax = arr[length+1-k]
    return(kthMin,kthMax)

arr = [3,5,7,9,8,15,10]
kth_min,kth_max = kthMinMax(arr,len(arr)-1,3)
print("kth_min",kth_min)
print("kth_max",kth_max)
