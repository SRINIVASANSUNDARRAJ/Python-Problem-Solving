num=int(input("Enter the number:"))
factorial=1
if num<0:
    print("sorry factorial doesnot exist")
if num ==0:
    print("the factorial for 0 is 1")
if num >1:
    for i in range(1,num+1):
        factorial=factorial*i
    print(f"factorial for {num} this number is {factorial}")