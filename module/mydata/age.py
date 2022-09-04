def year(n):
    if(n>=18):
        print("eligible for voting")
    elif(18>n<=10):
        print("not eligible for voting")
    else:
        print("for voting wait",18-n,"years")