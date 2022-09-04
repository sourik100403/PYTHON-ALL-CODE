text=input("enter a string")
vowel=0
for i in text:
    if i in "aeiouAEIOU":
        vowel+=1
print("no of vowel are",vowel)