#4)Write a program that computes the decimal equivalent of the binary number 10011?
'''
binary=input("enter a binary number")
decimal=0
for digit in binary:
    decimal=decimal*2+int(digit)
print(decimal)'''

while True:

    binary = input("Enter number in Binary Format: ")
    if binary == 'x':
        exit()
    else:
         decimal = int(binary, 2)
         print(binary,"in Decimal =",decimal)