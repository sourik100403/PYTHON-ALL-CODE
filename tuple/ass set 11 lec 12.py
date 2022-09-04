markesdict={}
english_val=input("enter your english markes")
phyics_val=input("enter your phyics markes")
math_val=input("enter your math markes")
chemistry_val=input("enter your chemistry markes")
history_val=input("enter your history markes")
markesdict["english"]=english_val
markesdict["phyics"]=phyics_val
markesdict["math"]=math_val
markesdict["chemistry"]=chemistry_val
markesdict["history"]=history_val
print(markesdict)
worst_key=min(markesdict,key=markesdict.get)
print("minimum value",worst_key,"with score",markesdict[worst_key])

highest_key=max(markesdict,key=markesdict.get)
print("minimum value",highest_key,"with score",markesdict[highest_key])