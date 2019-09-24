#8)Write a function called is_abecedarian that returns True if the letters in a word appear
# in alphabetical order (double letters are ok). How many abecedarian words are there?
# (i.e) "Abhor" or "Aux" or "Aadil" should return "True" Banana should return "False"




def is_abecedarian(string):

    for i in range(0,len(string)):
        for j in range(i+1,len(string)):
            if string[i]>string[j]:
                return False
    return True

string=input("Enter a string : ").lower()
print(is_abecedarian(string))