#Kadane's Algo [V.V.V.V.V IMP]
def Kadane(arr):
    msf=0
    meh=0
    for i in range (len(arr)):
        meh=meh+arr[i]
        if meh<0:
            meh=0
        if msf<meh:
            msf=meh
    print(msf) 

arr=[4,1,-2,1]
Kadane(arr)       

#FOR ANY SUGGESTIONS YOU ARE WELCOME 