'''def sayhello():
    print("hello venu")
sayhello()'''

'''def printintger(a):
    print("the value",a)

printintger(4)'''

#function with arguments
'''
def sum(a,b):
    a+b
    return a+b

res=sum(1,2)

if res>0:
    print("all the best")
else:
    print("try again")'''

#function within function
'''
def sum(a,b):
    c=a+b
    return c

def total():
    tot=0
    c=sum(5,5)
    if c==10:
        tot=c+1
        print(tot)

total()'''

def sum(a,b):
    c=a+b
    return a,b,c

temp1,temp2,temp3=sum(1,5)
print(temp1)
print(temp2)
print(temp3)


