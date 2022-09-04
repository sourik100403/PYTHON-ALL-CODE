class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=f"{fname}.{lname}@codewith haryy"
    def explain(self):
        return f"the employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "please set.......... the email by buseing the setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"
    @email.setter
    def email(self,string):
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
hindu_sup=employee("hindu","sup")
print(hindu_sup.email)
hindu_sup.fname="us"
print(hindu_sup.email)
hindu_sup.email="this.that@codewithharry.com"
print(hindu_sup.fname)
print(hindu_sup.lname)
del hindu_sup.email
print(hindu_sup.email)
hindu_sup.email="harry.perry@codewithhary.com"
print(hindu_sup.email)