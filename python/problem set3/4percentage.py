# 4) Modify the above program to print only the words that have no “e”
#    and compute the percentage of the words in the list have no “e.”
'''
def has_no_e(l):
    cnt=0

    for i in l:
        if 'e' not in i:
           print (i)
           cnt+=1
    print("No. of words not having e  ",cnt)
    print(len(l))
    per=(cnt/len(l))*100
    print("%.f"%per+"%")

list1=[]
list1=input("Enter the list of words : ").split(" ")
has_no_e(list1)


'''




# 4) Modify the above program to print only the words that have no “e”
#    and compute the percentage of the words in the list have no “e.”

def has_no_percent(l):
    count=0
    for i in l:
        if 'e' not in i:
            print(i)
            count+=1
    print("words which are not having e",count)
    print(len(l))
    per=(count/len(1))*100
    print("%.f"%per+"%")

list1=[]
list1=input("enter a string").split(" ")
has_no_percent(list1)