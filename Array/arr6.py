#Find the Union and Intersection of the two sorted arrays.
def uAi(arr1,arr2):
    a = arr1+arr2
    union=set(a)
    print("Union:",list(union))
    intersection=[]
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                intersection.append(a[j])
    print("Intersection:",intersection)
arr1=[1,2,3,4,5]
arr2=[3,4,5,6,7]
uAi(arr1,arr2)

#FOR ANY SUGGESTIONS YOU ARE WELCOME