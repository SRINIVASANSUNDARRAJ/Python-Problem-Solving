n=int(input("number of element:"))
print("enter the numbers")
a=[]
for i  in range(n):
    a+=[int(input())]
print(a)
for i in range(n):
    for j in range(i+1,n):
        if a[i]>=a[j]:
            a[i],a[j]=a[j],a[i]
print(a)
b=set(a)
print(b)
print(b[len(b)])
