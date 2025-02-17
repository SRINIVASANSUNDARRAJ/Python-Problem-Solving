n=int(input("enter the number :"))
fact=1
if(n<0):
    print("enter positive number")
if(n==0):
    print("the fact value is 1")
if n>1:
    for i in range(1,n+1):
        fact*=i
print(fact)


