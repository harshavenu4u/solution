'''A palindrome is a word that is spelled the same backward and forward, like "Malayalam" and "Noon" .
Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.
Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise.
Remember that you can use the built-in function len to check the length of a string.
Use the function definition
def isPalindrome(s):
	Assumes s is a str
	Returns True if s is a palindrome; False otherwise.
	Punctuation marks, blanks, and capitalization are
	ignored.'''

def ispalindrome(s):
    revstring=""
    for i in s:
        revstring=i+revstring
    if revstring==s:
         return True
    else:
         return False

string=input("enter a string").lower()
if ispalindrome(string):
    print("palindrome")
else:
    print("not a palindrome")
