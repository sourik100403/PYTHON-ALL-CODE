# list1=["code","with","harry"]
# for index,value in enumerate(list1):
#     print(index,value)
list2=["python","program","is","a","fun"]
result=enumerate(list2,10)
print(list(result))
list3=["alue","chilli","water million","bringel","ygyds"]
# i=0
# for item in list3:
#     if i%2 is not 0:
#         print(f"jarvis buy {item}")
#     i+=1
for index,item in enumerate(list3):
    if index%2==0:
        print(f"buy {item}")