
'''Write a program that examines three variables—x, y, and z— and
prints the largest odd number among them. If none
of them are odd, it should print a message to that effect.'''


x=int(input("enter x values"))
y=int(input("enter y values"))
z=int(input("enter z values"))
max=0
list1=[]
if x%2!=0:
    list1.append(x)
if y%2!=0:
    list1.append(y)
if z%2!=0:
    list1.append(z)
for i in list1:
    if i>max:
        max=i
if max>0:
    print(max)
else:
    print("all are even numbers")







