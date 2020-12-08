#Move all the negative elements to one side of the array 
def rearrange(arr,n):
    j=0
    for i in range(0,n):
        if arr[i]<0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    print(arr)
arr=[-3,4,-6,2,-8,-9]
rearrange(arr,len(arr))

#FOR ANY SUGGESTIONS YOU ARE WELCOME