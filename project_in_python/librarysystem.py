class Library:
    def __init__(self,list,name):
        self.bookList=list
        self.name=name
        self.lendDict={}
    def displayBook(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.bookList:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"book is alredy being used by {self.lendDict[book]}")
    def addBook(self,book):
        self.bookList.append(book)
        print("book has been added to the book list")
    def returnBook(self,book):
        self.lendDict.pop(book)
if __name__ == '__main__':
    sourik=Library(['python','basic c','DSA','math','react'],'souriklibrary.com')
    while(True):
        print(f"********Welcome to the {sourik.name} library+++++++")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice=input("enter your choice::")
        if user_choice not in ['1','2','3','4']:
            print("please enter valid input")
            continue
        else:
            user_choice=int(user_choice)
        if user_choice==1:
            sourik.displayBook()
        elif user_choice==2:
            book=input("enter the name of the book:")
            user=input("enter your name")
            sourik.lendBook(user,book)
        elif user_choice==3:
            book=input('enter the name of the book, you can add::')
            sourik.addBook(book)
        elif user_choice==4:
            book=input('enter the name of the book:')
            sourik.returnBook(book)
        else:
            print("enter valid input")
        print("press q to quit and c to continue")
        user_choice2=""
        while(user_choice2!="q" and user_choice2!="c"):
            user_choice2=input()
            if user_choice2=='q':
                exit()
            elif user_choice2=='c':
                continue