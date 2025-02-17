a_list=[]
n=int(input("enter the number number of element:"))
for i in range(0,n):
    element=int(input())
    a_list.append(element)
new_list=[]
for i in a_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)