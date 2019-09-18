def is_power(a,b):
    c=a/b
    if ((a%b==0)and (c%b==0)):
        return True
    else:
        return False


a=int(input("enter first number: "))
b=int(input("enter second number: "))
if(is_power(a,b)):
    print(a," is power of ",b)
else:
    print(a, " is not power of ", b)
