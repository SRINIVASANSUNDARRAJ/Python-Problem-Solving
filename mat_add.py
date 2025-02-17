R=int(input("enter the number:"))
c=int(input("enter the number:"))
matrix_a=[]
matrix_b=[]
result=[[0,0,0],[0,0,0,],[0,0,0]]
print("enter the entries:")
for i in range(R):
    a=[]
    for j in range(c):
       #a.append(int(input()))
       a+=[int(input())]
    matrix_a.append(a)
for i in range(R):
    for j in range(c):
        print(matrix_a[i][j],end=" ")
    print()

print("enter the elements:")
for i in range(R):
    b=[]
    for i in range(c):
        b.append(int(input()))
    matrix_b.append(b)
for i in range(R):
    for j in range(c):
        print(matrix_b[i][j],end=" ")    
    print()
for i in range(c):
    for j in range(len(matrix_a[0])):
        result [i][j]=matrix_a[i][j]+matrix_b[i][j]
print("resultant matrix:")
for r in result:
   
    print(r)