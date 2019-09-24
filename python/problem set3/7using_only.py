def using_only(word,list):
    for i in list:
        if i not in word:
            return False
    return True


word=input("Enter a word: ")
list1=[]
list1=input("enter a string of letters: ").split(" ")
if using_only(word,list1):
    print(word,"contains all the letters in the list")
else:
    print(word, "not contains all the letters in the list")
