input_string=input("enter the word: ")
#input_string=list(input_string)
my_set=set(input_string)

for char in my_set:
    count=0
    for element in input_string:
        if char == element:
            count+=1
        
    print(f"{char} is occurse {count}")

        