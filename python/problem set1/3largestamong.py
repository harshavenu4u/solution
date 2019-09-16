list1 = input('Enter 10 numbers with space').split()
odd_list = []
if len(list1)==0:
    print('Enter some values')
else:
    for i in list1:
        if int(i) % 2 != 0:
            odd_list.append(int(i))
    max = odd_list[0]
    if len(odd_list) != 0:
        for i in odd_list:
            if i > max:
                max = i
        print('Max ODD value:', max)
    else:
        print('None of the are odd values')
