input_string=[6,5,7,4,3,5,6,7,8,4,3,5]
print("The given input string is:",input_string)
charcount=dict()
mylist=[]
for character in input_string:
    if character in charcount:
        charcount[character]+=1
    else:
        charcount[character]=1
    mylist+=[character]
x=charcount.get(8)
print(x)
print(f"\nthe character count is:",charcount)
