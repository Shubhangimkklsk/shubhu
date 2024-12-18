#WAP to get the factorial of number uisng function
num=5
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(num)
print(result)
#output=120
#WAP to find maximum among two number
num1=int(input("enter 1st number:"))

num2=int(input("enter 2nd number:"))
def max():
    if num1 > num2:
        print("maximum number is=",num1)
    else:
        print("maximum number is=",num2)
result=max()
#WAP to check whether person can vote or not using function
age=int(input("Enter your age="))
def vote():
    if age>18:
        print("you can vote",age)
    else:
        print("you cannot vote",age)
votting=vote()
#WAP to get table of a number using function
num=5
def table():
    for i in range(1,11):
        print(num*i)
result=table()







