s=set([11,22,99])
t=set([66,22,11])
s.update(t)
print(s)
s.add(99)
print(s)
s.remove(22)
print(s)