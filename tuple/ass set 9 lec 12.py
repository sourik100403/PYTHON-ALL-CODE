cricket={'sachin':102,'rohit':88,'virat':99,'nehara':89}
name=input("enter the crickter name")
if name in cricket:
    print("run of",name,"player is",cricket[name])
else:
    print("player did not any score today")