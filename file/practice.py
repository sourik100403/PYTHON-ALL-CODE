f=open("myfile2","r")
text=f.read()
vowel=0
for i in text:
    if(i in "aeiouAEIOU"):
        vowel=vowel+1
print("total vowel=",vowel)
