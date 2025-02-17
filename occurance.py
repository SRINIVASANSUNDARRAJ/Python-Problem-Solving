input_string="MAXEYE TECHNOLOGIES."
print("The input string is:",input_string)
mySet=set(input_string)
for element in mySet:
    countofchar=0
    for character in input_string:
        if character is element:
            countofchar+=1
    print(f"Count of char '{element}' is {countofchar}")