#find Largest sum contiguous Subarray [V. IMP]
def maxsubarr(arr):
    maxSoFar=0
    maxEndingHere=0
    start=end=0
    beg=0
    for i in range(len(arr)):
        maxEndingHere=maxEndingHere+arr[i]
        if maxEndingHere<0:
            maxEndingHere=0
            beg =i+1
        if maxSoFar<maxEndingHere:
            maxSoFar=maxEndingHere
            start=beg
            end=i
    print("The sum of contiguous sublist with the largest sum is", maxSoFar)
    print("The contiguous sublist with the largest sum is", arr[start: end + 1])
 
arr=[-2,1,-3,4,-1,2]
maxsubarr(arr)

#FOR ANY SUGGESTIONS YOU ARE WELCOME
