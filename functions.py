###functions
##def myfun():
##    print("hello")
##myfun()
##
##def add(a,b):
##    ans=a+b
##    print("anser is",ans)
##add(65,58)
##
##c=int(input("enter number"))
##d=int(input("enter number"))
##add(c,d)

#area of rectanglr
##l=int(input("enter the length of rectangle"))
##w=int(input("enter the width of rectangle"))
##def rect(l,w):
##    area=l*w
##    print("area of a rectangle is",area)
##rect(l,w)

#wap to get area of circle
##a=int(input("enter radius"))
##def cir(a):
##    area2=3.14*a*a
##    print("area of a circle is",area2)
##cir(a)
###wap to remove duplicate from the list
##def rem_dup(l):
##    print(list(set(l)))
##l=[78,65,45,21,44,55,55,55]
##rem_dup(l)
###when to use return
##def rem_dupl(b):
##    return list(set(b))
##b=[78,67,52,11,11,23,33,33]
##ans=rem_dup(b)
##print("the clean data set without any duplicate",ans)
#wap to get factorial of a number
print("25-11-24 functions")

##nm="shubhu"
##id=23
##def p1():
##    print("welcome",nm,id)
##p1()


##class userinfo:
##    def pudata(self):
##        self.name=input("enter your name:")
##        self.id=int(input("enter your id:"))
##        self.salary=float(input("enter your salary:"))
##    def display(self):
##        print("your name=",self.name)
##        print("your id=",self.id)
##        print("your salary=",self.salary)
##obj=userinfo()
##obj.pudata()
##obj.display()


##class student:
##    def __init__(self,name,age,grade):
##        self.name=name
##        self.age=age
##        self.grade=grade
##
##    def display(self):
##        print(f"name:{self.name},Age:{self.age},Grade:{self.grade}")
##
##student1=student("shubhu",12,"5th")
##student2=student("shubhu",16,"9th")
##
##student1.display()
##student2.display()

##print("wap to print bookdata as title,year,author etc witg vlass and objrct")
##
##class book:
##    def __init__(self,title,year,author):
##        self.title=title
##        self.year=year
##        self.author=author
##
##    def display(self):
##        print(f"Title:{self.title},Year:{self.year},author:{self.author}")
##book1=book("abc",2008,"bbb")
##book2=book("xyz",2009,"ccc")
##
##book1.display()
##book2.display()


print("creation of simple application")


class bankacc:
    def __init__(self,initialAmt,accHolder):
        self.balance=initialAmt
        self.name=accHolder
        print("account created")
        print(f"acount created for:'{self.name}' with opening balance={self.balance}")
    def getData(self):
        print(f"acount created for:'{self.name}' with opening balance={self.balance:.2f}")

    def deposite(self,amount):
        self.balance=self.balance+amount
        print("amount deposited successfully")
        self.getData()
        print("thank you")
        
    def withDraw(self,amount):
        
        self.balance=self.balance-amount
        print("amount withdraw successfully")
        print("your remaining balance is ",self.balance)
        
      































