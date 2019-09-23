def is_anagram(str1,str2):
    if len(str1)!=len(str2):
        return False

    if sorted(str1)==sorted(str2):
        return True
    else:
        return  False


first=input("enter first string")
second=input("enter second string")
check=is_anagram(first,second)
if check:
    print("it is anagram")

else:
    print("not anagram")