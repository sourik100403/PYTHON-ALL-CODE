import json
data='{"var1":"harry","var2":56}'
print(data)
data2={
    "channel":"codewithharry",
    "cars":["bmw","audi"],
    "isbad":False
}
print(data2)
jscomp=json.dumps(data2)
print(jscomp)