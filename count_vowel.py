vowel="aeiou"
vowel=list(vowel)
word=input("enter the word:")
count=0
for character in word:
    if character in vowel:
        count+=1
print(count)