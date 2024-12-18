#Create dynamic list where you will ask user to enter 5 elements in it and perform insert new element and delete an element operation on it.
num=[]
print("please enter 5 elements")
for i in range(5):
    element=input(f"enter element{i+1}:")
    num.append(element)
print(num)


while True:
    print("\n choose an option")
    print("1.Insert a new element")
    print("2.Delete an element")
    print("3.Exit")

    choice=int(input("enter your choice:")
     if choice=="1":
               new_element=input("enter new element:")
               position=int(input("enter the position",len(num)))
    
