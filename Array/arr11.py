#find duplicate in an array of N+1 Integers
def duplicate(arr,n):
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                print(arr[j])
#other approach
arr=[1,2,2,4,6,7,3,4,9]
duplicate(arr,len(arr))

class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


#FOR ANY SUGGESTIONS YOU ARE WELCOME            