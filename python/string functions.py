'''string="accenture"
x=string.capitalize() #capitalize first letter
print(x)

string1="ACCENTURE"
x1=string.casefold() # converts in to lower case
print(x1)

x=string.upper()
print(x)

x1=string1.lower()
print(x1)

x=string[2:5]
print(x)

x=string[-2:-5]
print(x)

print(len(x))

x=string1.center(15) #moves the postion of string
print(x)'''
a=int(input("enter start value"))
b=int(input("enter end value"))
even_sum=0
odd_sum=0
for i in range(a,b):
    if i%2==0:
        even_sum=even_sum+i

    else:
        odd_sum=odd_sum+i
print(even_sum)
print(odd_sum)





