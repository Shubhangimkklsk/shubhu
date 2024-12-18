print("list comprihension")
marks=[20,34,567,78,678]
new_marks=[]#empty list
for i in marks:
    new_marks.append(i+2)
print(new_marks)
print("----------------------------------------")
marks=[20,34,567,78,678]
for i in marks:
    print(i+2)


print("----------------------------------------")
cubes=[]
for i in range(11):
    if i%2==0:
        cubes.append(i**3)
print("listing for loops",cubes)
print("----------------------------------------")
easy=[i**3 for i in range(10) if i%2==0]
print(easy)
print("----------------------------------------")
set1={61,54,58,78}
for i in set1:
   print(i+2)
print("----------------------------------------")
  
set1={61,54,58,78}
new={i+2 for i in set1}
print(new)
