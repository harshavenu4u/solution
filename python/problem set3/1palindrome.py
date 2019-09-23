def is_palindrome(s):
    if s==s[::-1]:
        return ("true")

    else:
        return ("false")

string=input("enter a string")
check=is_palindrome(string)
if check:
    print("is is a palindrome")
else:
    print("not a palindrome")