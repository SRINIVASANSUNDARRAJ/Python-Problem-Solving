def findpeak(arr,n):
    if(n==1):
        return 0
    if (arr[0]>=arr[1]):
        return 0
    if (arr[n-1]>=arr[n-2]):
        return n-1
    for i in range(1,n-1):
        if (arr[i]>=arr[i-1] and arr[i]>=arr[i+1]):
            return i
arr=[1,3,36,78,45,0]
n=len(arr)
print("Index of a peak point",findpeak(arr,n))

