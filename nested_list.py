num=[]
arr=[]
for i in range (int(input())):
    name=input()
    score=float(input())
    num.append([name,score])
    arr.append(score)
num.sort()
second_mini=0
mini=num[0]
arr.sort()
for i in num:
    if i!=mini:
        second_mini=i
        break
for i in arr:
    if i[1] == second_mini:
        print(i[0])