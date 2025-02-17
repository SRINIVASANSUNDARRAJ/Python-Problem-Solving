num=int(input("Enter the number:"))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag= True
            break
    if flag is True:
        print(f"{num} is not prime number")
    else:
        print(f"{num} is prime number")
        