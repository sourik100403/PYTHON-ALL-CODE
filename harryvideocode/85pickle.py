import pickle
# car=["audi","tata nano","maruti suzuki","toyota"]
# file="mycar.pkl"
# fileobj=open(file,'wb')
# pickle.dump(car,fileobj)
# fileobj.close()

#unpickleing
file="mycar.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))