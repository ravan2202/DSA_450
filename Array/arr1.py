#Reverse the array
def reverse(arr,start,end):
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start] 
        start+=1
        end-=1

arr=[1,2,3,4,5]
reverse(arr,0,len(arr)-1)
print(arr)

# we can also use reverse function

#FOR ANY SUGGESTIONS YOU ARE WELCOME