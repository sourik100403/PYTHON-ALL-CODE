import time
initial=time.time()
k=0
while(k<45):
    print("HAPPY NEW YEAR")
    #time.sleep(2)
    k+=1
print("while run in",time.time()-initial,"second")
initial1=time.time()
for i in range(45):
    print("SRITIKONA GHOSH")
print("for run in",time.time()-initial1,"second")
today=time.asctime(time.localtime(time.time()))
print(today)