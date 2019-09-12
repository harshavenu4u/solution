'''i=1
for i in range(1,10,-1 ):
    print(i)'''

'''
a=int(input("enter start value"))
b=int(input("enter end value"))
for a in range(b):
    print(a)'''

''' sum of even and odd number
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
print(odd_sum)'''

''' length of a string

str="welcome"
count=0
for i in str:
    count=count+1
    print(count)'''

'''
str="welcome"
if "e" in str:
    print("yes")'''

''' counting same character in the string
str="welcome"
count=0
for i in str:
    if  i=="e":
        count=count+1
print(count) '''

'''str="welcome"
count=0
for i in str:
    if i=="l":
        print(str)'''

'''
num=[]
for i in range(1,10):
    if i%2==0:
        num.append(i)
print(num)'''

'''
list1=[1,'a',2,'b']
digit_count=0
char_count=0

for i in list1:
    if type(i)==int:
        digit_count=digit_count+1

    else:
        char_count=char_count+1
print(digit_count)
print(char_count)'''


'''
list1=[1,'a',2,'b']
digit_count=0
char_count=0
for i in list1:
    if ord(str(i))>65 and ord(str(i))>95:
        char_count=char_count+1
    else:
        digit_count = digit_count + 1
print(digit_count)
print(char_count)'''

'''
for i in range(1,10):
    for j in range(1,10):
        print(j)'''

'''
for i in range(1,10):
    for j in range(1,i):
        print(j,end=" ")
    print("\n")'''

'''
for i in range(1,6):
    for j in range(1,i):
        print("*",end=" ")
    print("\n")'''

'''
for i in range(5):
    for j in range(5-i):
        print(j,end=" ")
    print()'''

''
n=int(input("enter a value"))
for i in range(1,n):
    for j in range(0,i):
        print(j,end=" ")
    print()

'''i=1
while(i<=5):
    print(i)
    i=i+1'''

'''
#break  and continue statement
for i in range(1,6):
    if(i==3):
        break
    else:
        print(i)
print("you have reached the limit")
print("bye")'''










