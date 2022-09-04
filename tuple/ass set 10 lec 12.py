d={'a':3,'b':1,'c':100}
best_key=min(d,key=d.get)
print(best_key,d[best_key])
best_keys=max(d,key=d.get)
print(best_keys,d[best_keys])