'''
1
2 2
3 3 3
4 4 4 4
'''
n=int(input('enter a number'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()