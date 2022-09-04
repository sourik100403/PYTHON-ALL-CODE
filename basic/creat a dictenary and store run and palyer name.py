s={}
n=int(input("enter the no of player"))
for i in range(n):
    x=input("player name :")
    s[x]=input("player runs scored :")
    p=input("\n search the player name :")
    if(p not in s):
        print("not found")
    else:
        print("score run is", s[p])
print(S)