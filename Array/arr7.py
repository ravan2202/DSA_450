#Write a program to cyclically rotate an array by one.
def cyc(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
    print(arr)

arr=[1,2,3,4,5]    
cyc(arr,len(arr))

#FOR ANY SUGGESTIONS YOU ARE WELCOME