#Write a function named avoids that takes a word and a string of forbidden letters
# , and that returns True if the word doesn’t use any of the forbidden letters.

def forbidden(word, stringHere):
    for letters in word:
        if stringHere in word:
            return False
    return True

word=input("enter a word")
string=input("enter a string")
print(forbidden(word,string))