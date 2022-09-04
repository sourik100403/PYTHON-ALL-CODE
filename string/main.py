#sender=abc get=def
msg="girl"
i=0
while(i<len(msg)):
    letter=msg[i]
    print(chr(ord(letter)+3),end='')
    i=i+1