#set
# a=[]
# for i in range(100):
#     if i%3==0:
#         a.append(i)
# print(a)
# a=[i for i in range(100) if i%3==0]
# print(a)
#
# #dict
# dict1={i:f"item{i}" for i in range(100) if i%5==0}
# dict2={value:key for key,value in dict1.items()}
# print(dict1)
# print(dict2)

# dress={dress for dress in ["a","b","c","a","a","b"] }
# print(dress)

#generator
# def gener(n):
#     for i in range(n):
#         yield i
# a=gener(5)
# print(a.__next__())
# print(a.__next__())
evens = (i for i in range(100) if i%2==0)
print(evens.__next__())

for item in evens:
    print(item)