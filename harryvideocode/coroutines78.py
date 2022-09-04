# def func():
#     print("code with harry")
#     while True:
#         value=(yield)
#         print(value)
# coroutines=func()
# next(coroutines)
# coroutines.send("python")
# coroutines.send("tutorial")
# coroutines.close()
def search():
    import time
    book="this is book of harry website"
    time.sleep(4)
    while True:
        text=(yield)
        if text in book:
            print("this is on book")
        else:
            print("this is not in book")
sea=search()
print("search start")
next(sea)
print("next method run")
sea.send("harrykjku")
sea.close()