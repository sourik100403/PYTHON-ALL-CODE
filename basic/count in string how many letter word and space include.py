s=input("enter the string")
dig=0
let=0
word=0
for c in s:
    if c.isdigit():
        dig=dig+1
    elif c.isalpha():
        let=let+1
    elif c==" ":
        word=word+1
    else:
        pass
print("letter",let)
print("digit",dig)
print("space",word)