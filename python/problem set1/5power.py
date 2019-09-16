n=int(input("enter a number"))
for i in range(1,6):
    root=i ** (1/i)
    if int(root) ** i == n:
        print('root', root, 'power', i)
        break
print('No power and roots are  found')

