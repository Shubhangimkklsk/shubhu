###list is collection ehich is ordered and changeable
###allows duplicate
##my_list=["soap",123,"maggie","aman"]
##print(my_list)
##for i in my_list:
##    print(i)
##my_list.append("dalia")
##print(my_list)
##print("____________________________________________")
###list element is recognized by its index value
###first element my_list(0)
##print(my_list[0])
###there is concept of negative indexing
##print(my_list[-1])
###slicing
##
##print(my_list[1:4])
##print(my_list[2:4])
##print(my_list[4:6])
##print(my_list[2:5])
##print(my_list[::-1])
##print("____________________________________________")
##marks=[52,65,89,98,102]
##print(min(marks))
##print("the maximum value is",max(marks))
#wap to find second largest number
##for i in range(0,5):
##    for j in range(i+1,5):
##        if marks[j]>marks[i]:
##            temp=marks[i]
##            marks[i]=marks[j]
##            marks[j]=temp
##print(marks)
##print(marks[1])








#13-11-24
#while loop is used to repeat particular block of sentence agian and again
###wap to print hello 10 times
##i=1
##while(i<=10):
##    print("hello")
##    i+=1
###wap to generate table of a number
##n=int(input("enter a number "))
##
##i=1
##while(i<=10):
##    ans=n*i
##    print(ans)
#wap to reverse a given number
##n=int(input("enter a number"))
##rev=0
##while(n>0):
##    rem=n%10
##    rev=rev*10+rem
##    n=n//10
##print("reverse=",rev)






#14-11-24 dictionaries
#Dictionary is 
'''a dictinory is a built in data structure in python that allows you to store a collection of key value pairs'''
my_dict={
    "std_id":123,
    "std_name":"sameera",
    "course":"BCA"
}
print(my_dict)

x=my_dict["course"]
print("the course selected is",x)

x=my_dict.get("std_id")
print(x)

#find all the keys present in the dictionary

y=my_dict.keys()
print("the keys present are:",y)

my_dict.update({"std_name":"sameer"})
print(my_dict)

#to add a new feild in dictionary

my_dict["fees"]=76000
print(my_dict)

my_dict["student_add"]="thane"
print(my_dict)

#to remove certain element from the dictionary
my_dict.popitem()
print(my_dict)
print("____________________________________________")
#looping over dictory
for i in my_dict:
    print(i)
print("____________________________________________")
#to get keys from the dictoney
for i in my_dict.keys():
    print(i)
print("____________________________________________")
#to get values from the list
for i in my_dict.values():
    print(i)
print("____________________________________________")

for x,y in my_dict.items():
    print(x,y)

print("____________________________________________")

#wap to get some of digits present in a number
##num=int(input("enter number"))
##sum=0
##while(num>0):
##    rem=num%10
##    sum=sum+rem
##    num=num//10
##print("the sum of the number is",sum)

print("____________________________________________")
#wap to check whether the number is armstrong numb or not
##num=int(input("enter any number"))
##s=num
##b=len(str(num))
##sum1=0
##while num!=0:
##    r=num%10
##    sum1=sum1+(r**b)
##    num=num//10
##if s==sum1:
##    print("the number is armstrong",s)
##else:
##    print("the given numbr is not armstrong",s)
'''
set in Python programming is an unordered collection data type that is iterable and has no duplicate
elements'''
set_q={1,2,3,4}
print(set_q)

set_b={7,8,9,4}
print(set_b)

#union
##set_d=set_q.union(set_b)
##print(set_d)
###using union operator |
#result=set_q|set_b
##print(result)
##print(type(set_q))
#using intersection

##result=set_q.intersection(set_b)
##print(result)

result=set_q&set_b
print(result)

#difference 

result=set_q-set_b
print(result)

result=set_q.difference(set_b)
print(result)


