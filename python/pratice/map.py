#map
'''input=[1,2,3,4]
print(map(lambda a:a*2,input))
output=list(map(lambda a:a*2,input))
print(output)'''


'''
#filter
input=[-5,-4,-3,-2,1,2,3,4]
output=list(filter(lambda a:a<0,input))
print(output)'''

'''

input=["a","b","c","d","e","f","g","h","i","j"]
vowels=["a","e","i"]
output=list(filter(lambda a:a not in vowels,input))
print(output)
'''


string="accenture"
output=map(lambda cnt:cnt+"1",string)
print(output)
1print("".join(output))


'''
from functools import reduce

list1=[1,2,3,4]
out=reduce(lambda arg1,arg2:arg1*arg2,list1)
print(out)'''

string="11684151"
out=list(map(lambda i:i*2,string))
print("".join(out))