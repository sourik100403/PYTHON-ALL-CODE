f1=open("sourik.txt","r")
print(f1.read())
f1.close()

f1=open("sourik.txt","r")
text=f1.read()
vowel=0
for i in text:
    if(i in "aeiouAEIOU"):
        vowel=vowel+1
print("total vowel=",vowel)
f1.close()