student=(('ss',"cse",89.7),("pp","it",87.6),("kk","ece",67.5))
for i in student:
    print(i)
choice=input("do you want to edit the detalis")
if(choice=="y"):
    name=input("enter the old name you edit")
    new_name=input("enter new name")
    new_course=input("enter new course")
    new_markes=input("enter the new markes")
    i=0
    new_student=()
    while(i<len(student)):
        if(student[i][0]==name):
            new_student=new_student+(new_name,new_course,new_markes)
        else:
            new_student=new_student+student[i]
        i=i+1
for i in new_student:
    print(i,end=' ')