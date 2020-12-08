#Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

#Algorithm:
#At first, the full array is unknown. There are three indices – low, mid and high. Initially, the value of low = mid = 1 and high = N.
#If the ith element is 0 then swap the element to the low range, thus shrinking the unknown range.
#Similarly, if the element is 1 then keep it as it is but shrink the unknown range.
#If the element is 2 then swap it with an element in high range.
def sort0129(arr,n):
    low=0
    mid=0
    high=n-1
    while(mid<=high):
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            mid+=1
            low+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    print(arr)    

arr=[1,2,0,0,2,1,1]
sort0129(arr,len(arr))

#FOR ANY SUGGESTIONS YOU ARE WELCOME
