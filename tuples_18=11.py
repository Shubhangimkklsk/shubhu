'''ordered
when se say that tuples are ordered, it means that the items have a defined order, and that order will not change
unchangeable: tuples are unchangeable meaning that we cannot change, add or remove items after the tuple has creaded
allows duplicate
since tuples are indexed they can have items with the same value:
'''
##thistuple("apple","banana","cherry","apple")
##print(thistuple)
##
###find the length of the tuple
##print(len(thiatuple))
##
###tuple is also recognize by its index number
##print(thistuple[0])
##print(thistuple[3])
t1=("ditya",5000,"aman",54644)
print(t1)
print(type(t1))
print("tuple slicing")
print(t1[1:2])
print(t1[:3])
print("find length")
print("the length of a tupkeis:",len(t1))
print("negative indexing")
print(t1[-2])
print(t1[-1])
print("tuplke into list")
t2=list(t1)
print(t2)
t2[2]="a in aports"
print(t2)
for i in t2:
    print(i)
print("------------------------------------")
print("wap to reverse the given tuple")
tup1=(56,25,14,164,96)
print("the original tuple is:",tup1)
rev=(tup1[::-1])
print("the reverse order is :")
print(rev)
print("------------------------------------")
for i in tup1:
    if i%2==0:
        print(i)
    
tup2=(45,[65,85],50,60,40,80)
print(tup2[0])
print(tup2[1])
print(tup2[1][0])
print(tup2[1][1])
tup2[1][0]=45
print(tup2)
print("wap to count the 45 in the tuple")
print("the 45 occurs ",tup2.count(45),"times")
print("------------------------------------")
print("wap to create tuple with diffrent data types")
tup3=("maggie",3,15,20,85,True)
print("i want to eat maggie",tup3)

marks=23,67,87,34
print("i have got marks as:")
print(marks)

#wap to create tuple with single item
price=34,
print(price)

















