n=int(input("enter n for n*n:"))
a=[]
b=[]
print("enter the elements:")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    a.append(row)
for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    b.append(row)
for i in range(n):
    for j in range(n):
        print(b[i][j],end=" ")
    print()
for k in a,b:
    print(k)