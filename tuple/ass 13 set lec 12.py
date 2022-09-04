a={}
n=int(input("Enter how many players"))
for i in range(0,n):
    name=input("Enter player name::")
    score=int(input("enter score::"))
    a[name]=score
print(a)
search_value=input("Enter name of player::")
if(search_value in a.keys()):
    print("Score is::",a[search_value])
else:
    print("Player not found")
