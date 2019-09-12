list1=['five',5,'six',6,'seven',7,'seven',7.5,'nine',9]
#list2=['five','six','seven','seven','nine']
#list3=[5,6,7,7.5,9]
dict1={}
dict_key=[]
dict_values=[]

for i in list1:
    if type(i)==str:
         dict_key.append(i)
    else:
         dict_values.append(i)

for i in range(len(dict_key)):
    if dict_key[i] not in dict1:
        dict1[dict_key[i]]=dict_values[i]
    else:
        li=[dict1[dict_key[i]],dict_values[i]]
        dict1[dict_key[i]]=li

print(dict1)

