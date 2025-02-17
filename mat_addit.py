R=int(input("enter the number:"))
c=int(input("enter the number:"))
r=[[0,0,0],[0,0,0],[0,0,0]]
mat_a=[]
mat_b=[]
print("put entries:")
for i in range(R):
    a=[]
    for j in range(c):
       #a.append(int(input()))
       a+=[int(input())]
    mat_a+=[a]
for i in range(R):
    for j in range(c):
        print(mat_a[i][j],end=" ")
    print()
for i in range(R):
    b=[]
    for j in range(c):
        b+=[int(input())]
    mat_b+=[b]
for i in range(R):
    for j in range(c):
        print(mat_b[i][j],end=" ")
    print()
for i in range(len(mat_a)):
    for j in range(len(mat_b[0])):
        for k in range(len(mat_b)):
            r[i][j]+=mat_a[i][k]*mat_b[j][k]
for k in r:
    print(k)

            