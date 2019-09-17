#5)Implement a function that meets the specification below. Use a try-except block.

#def sumDigits(s):
	#Assumes s is a string
	#Returns the sum of the decimal digits in s
	#For example, if s is 'a2b3c' it returns 5

string=input("enter sum of digit of a string" )
def sumdigits(s):

    sum=0
    for i in string:
        if i.isdigit():
            sum=sum+int(i)
    print(sum)

try:
    sumdigits(string)

except:
    print("error")
