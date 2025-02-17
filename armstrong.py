'''num=int(input("Enter the number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=pow(digit,3)
    temp=temp//10
if num == sum:
    print(num,"armstrong")
else:
    print(num,"not armstrong")'''
input_array=[1,3,5,7,9,8,6,4,2,4,6,8,9,7,5,7]
route=dict()
count=0
for i in input_array:
    if i in route:
        route[i]+=1
        count+=1
    else:
        route[i]=1
        count=1
if count==1:
    print(i)
print(route)
