"""3.Observe the following function definitions.
They Calculate the Factorial as per the Mathematical definition 1! = 1 (n + 1)! = (n + 1) * n!
Implement factI(n) as an Iterative Implementation & factR(n) as a Recursive Implementation"""


def factI(n):
    fact = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        fact =fact* i
    return fact


def fact1(n):
    if n == 0:
        return 1
    else:
        return n * fact1(n - 1)


num = 5
print(factI(num))
print(fact1(num))