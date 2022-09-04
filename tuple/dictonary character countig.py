msg="This Is pyThon class"
#msg=msg.lower()
dict1=dict()
for character in msg:
    if(character not in dict1):
        dict1[character]=1
    else:
        dict1[character]=dict1[character]+1
print(dict1)