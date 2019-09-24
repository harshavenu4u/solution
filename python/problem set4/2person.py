#2)Define a class Person and its two child classes: Male and Female.
# All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person:

    def getgender(self):
        print("unknown")

class Male(Person):
    def getgender(self):
        print("male")

class Female(Person):
    def getgender(self):
        print("female")

m=Male()
m.getgender()
f=Female()
f.getgender()