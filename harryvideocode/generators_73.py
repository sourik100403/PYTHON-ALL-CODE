def gen(n):
    for i in range(n):
        yield i
g=gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())

# h=6867
# ier=iter(h)
# print(ier._next_())

h="harry"
print(h.__iter__())
